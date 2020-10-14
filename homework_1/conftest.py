import pytest


@pytest.fixture(scope="function")
def creation_dictionary():
    items_dictionary = {1: "Bumblby", 2: 99.9, "3": True}
    return items_dictionary


@pytest.fixture(scope="function")
def creation_list():
    items_list = [1, 21, 2, 5, 'тест', 'pytest']
    return items_list


@pytest.fixture(scope="function")
def list_of_data():
    items_list = ["pytest", 5, 'i', ("один", 1), 6]
    return items_list


@pytest.fixture(autouse=True)
def remove_element():
    items_list = [1, 2, 5, 'тест']
    items_list.remove('тест')
    print(items_list)
    return items_list


@pytest.fixture()
def create_list():
    items_list = list(range(5))
    return items_list


@pytest.fixture(autouse=True)
def create_set():
    users = {"Mike", "Bill", "Ted"}
    return users


@pytest.fixture(autouse=True)
def create_frozen_set():
    users = frozenset({"Mike", "Bill", "Ted"})
    return users


@pytest.fixture
def add_unique_value():
    set_1 = {1, 2, 3, 4, 5}
    set_2 = {2, 3, 4, 5, 6}
    set_1.update(set_2)
    return set_1


@pytest.fixture(scope="function")
def сreate_text(request):
    print(f"\n from {request.scope} fixture!")
    text = "Pytest - тестовый фреймворк"
    return text


@pytest.fixture(scope="module")
def сoncatenate_text(request):
    print(f"\n from {request.scope} fixture!")
    first = "Pytest -"
    second = "тестовый фреймворк"
    text = first + " " + second
    return text
