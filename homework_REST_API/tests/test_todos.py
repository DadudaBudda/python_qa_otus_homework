import json
import os
import jsonschema
import pytest


def validate_jsonschema(data, schema_file):
    schema_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'schema')
    file = os.path.join(schema_dir, schema_file)
    with open(file) as json_schema:
        return jsonschema.validate(instance=data, schema=json.load(json_schema))


def test_listing_all_positive(session, base_url):
    response = session.get(url=base_url)
    assert response.status_code == 200


@pytest.mark.parametrize('title', ['', 'random', 'воплр', '@2134567865'])
@pytest.mark.parametrize('completed', [True, False])
@pytest.mark.parametrize('userId', [0, 10, 20])
def test_add_all(session, base_url, title, userId, completed):
    body = {'title': title, 'completed': completed, 'userId': userId}
    response = session.post(url=base_url, json=body)
    response = json.loads(response.text)

    assert response['userId'] == userId
    assert response['title'] == title
    assert response['completed'] == completed


def test_creating_negative(session, base_url):
    body = {'title': 454.e2433, 'completed': True, 'userId': 1}

    response = session.post(url=base_url, json=body)
    assert response.status_code == 500


@pytest.mark.parametrize('title', ['', 'random', 'воплр', '@2134567865'])
@pytest.mark.parametrize('completed', [True, False])
@pytest.mark.parametrize('userId', [0, 10, 20])
def test_update_positive(session, base_url, completed, title, userId):
    body = {'title': title, 'completed': completed, 'userId': userId}
    response = session.put(url=f'{base_url}/1', json=body)

    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['userId'] == userId
    assert response.json()['title'] == title
    assert response.json()['body'] == body


def test_update_negative(session, base_url):
    body = {'title': 454.e2433, 'completed': True, 'userId': 1}
    res = session.put(url=f'{base_url}/1', json=body)

    assert res.status_code == 500


@pytest.mark.parametrize('title', ['', 'random', 'воплр', '@2134567865'])
@pytest.mark.parametrize('completed', [True, False])
@pytest.mark.parametrize('userId', [0, 10, 20])
def test_update_positive(session, base_url, completed, title, userId):
    body = {'title': title, 'completed': completed, 'userId': userId}
    response = session.put(url=f'{base_url}/1', json=body)

    assert response.status_code == 200
    assert response.json()['id'] == 1
    assert response.json()['userId'] == userId
    assert response.json()['title'] == title
    assert response.json()['completed'] == completed


@pytest.mark.parametrize('id', [1, 10])
def test_deleting_resource_positive(session, base_url, id):
    response = session.delete(url=f'{base_url}/{id}')

    assert response.status_code == 200
    assert isinstance(response.json(), dict)


@pytest.mark.parametrize('userId', [-1, 12, 'test', None])
def test_filter_user_id_negative(session, base_url, userId):
    response = session.get(url=f'{base_url}/?userId={userId}')

    assert response.status_code == 200
    assert len(response.json()) == 0


def test_schema_todos(session, base_url):
    response = session.get(url=f'{base_url}')
    validate_jsonschema(data=response.json(), schema_file='todos.json')
