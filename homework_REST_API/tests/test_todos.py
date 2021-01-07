import math
import pytest

from homework_REST_API.conftest import ALL_TODOS


def test_listing_all_positive(session, base_url):
    response = session.get(url=base_url)

    assert response.status_code == 200
    assert len(response.json()) == ALL_TODOS


@pytest.mark.parametrize('id', [1, ALL_TODOS])
def test_get_positive(session, base_url, id):
    response = session.get(url=f'{base_url}/{id}')

    assert response.status_code == 200
    assert response.json()['id'] == id


@pytest.mark.parametrize('id', [0, ALL_TODOS + 1])
def test_get_negative(session, base_url, id):
    response = session.get(url=f'{base_url}/{id}')

    assert response.status_code == 404


@pytest.mark.parametrize('title', ['', 'random', 'воплр', '@2134567865'])
@pytest.mark.parametrize('completed', [True, False])
@pytest.mark.parametrize('userId', [0, 10, 20])
def test_add_all(session, base_url, title, userId, completed):
    body = {'title': title, 'completed': completed, 'userId': userId}
    response = session.post(url=base_url, json=body)
    response_json = response.json()

    assert response.status_code == 201
    assert response_json['userId'] == userId
    assert response_json['title'] == title
    assert response_json['completed'] == completed


def test_creating_negative(session, base_url):
    body = {'title': math.inf, 'completed': True, 'userId': 1}

    response = session.post(url=base_url, json=body)
    assert response.status_code == 500


def test_update_negative(session, base_url):
    body = {'title': math.inf, 'completed': True, 'userId': 1}
    response = session.put(url=f'{base_url}/1', json=body)

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
    assert response.json()['completed'] == completed


@pytest.mark.parametrize('id', [1, 10])
def test_deleting_resource_positive(session, base_url, id):
    response = session.delete(url=f'{base_url}/{id}')

    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.parametrize('field, value', [("userId", 2),
                                          ("id", 2),
                                          ("title", "sed et ea eum"),
                                          ("completed", 'true'),
                                          ("completed", 'false')])
def test_filter(session, base_url, value, field):
    response = session.get(url=f'{base_url}/?{field}={value}')
    response_json = response.json()

    if "completed" in field:
        if value == 'true':
            value = True

        else:
            value = False

    assert response.status_code == 200

    for _ in response_json:
        assert _[field] == value


@pytest.mark.parametrize('params',
                         [{"userId": -1}, {"userId": 12}, {"userId": 'test'},
                          {"id": 0}, {"id": 201}, {"id": 'test'},
                          {"title": ""}, {"completed": ""}])
def test_filter_negative(session, base_url, params):
    response = session.get(url=f'{base_url}', params=params)

    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.parametrize('field, value', [("userId", 1),
                                          ("id", 2),
                                          ("title", "asdfg"),
                                          ("completed", True)])
def test_patch(session, base_url, field, value):
    todo_id = 0
    if "id" in field:
        res = session.get(url=f'{base_url}/{value}')

    else:
        todo_id = "1"
        res = session.get(url=f'{base_url}/{todo_id}')

    response = session.patch(url=f'{base_url}/{todo_id}',
                             json={field: value})
    response_json = response.json()

    assert res.status_code == 200
    assert response_json[field] == value
