import math
import pytest

from homework_Selenium.conftest import ALL_TODOS


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


@pytest.mark.parametrize('user_id', [-1, 12, 'test', None])
def test_filter_user_id_negative(session, base_url, user_id):
    response = session.get(url=f'{base_url}/?userId={user_id}')

    assert response.status_code == 200
    assert len(response.json()) == 0


@pytest.mark.parametrize('item_id', [0, 201, None, 'test'])
def test_filter_id_negative(session, base_url, item_id):
    response = session.get(url=f'{base_url}/?id={item_id}')

    assert response.status_code == 200
    assert len(response.json()) == 0


def test_filter_completed_negative(session, base_url):
    response = session.get(url=f'{base_url}/?completed=')

    assert response.status_code == 200
    assert len(response.json()) == 0


def test_filter_title_negative(session, base_url):
    response = session.get(url=f'{base_url}/?title=')

    assert response.status_code == 200
    assert len(response.json()) == 0


def test_update_title(session, base_url):
    id = 1
    body = {'title': 'asdfg'}
    response = session.patch(url=f'{base_url}/{id}', json=body)

    assert response.status_code == 200
    response = response.json()

    assert response['id'] == id
    assert response['title'] == body['title']


def test_patch_user_id(session, base_url):
    id = 1
    new_user_id = 2
    res = session.get(url=f'{base_url}/{id}')
    body = {'userId': new_user_id}
    response = session.patch(url=f'{base_url}/{id}', json=body)

    assert res.status_code == 200
    response_json = response.json()

    assert response_json['id'] == id
    assert response_json['userId'] == new_user_id


def test_patch_todo_id(session, base_url):
    todo_id = 1
    new_todo_id = 2
    body = {'id': new_todo_id}
    response = session.patch(url=f'{base_url}/{todo_id}', json=body)

    assert response.status_code == 200
    response_json = response.json()
    assert response_json['id'] == new_todo_id
