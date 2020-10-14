import pytest


# Тест проверки доступности индекса по наименованию элемента списка
def test_index_value(creation_list):
    assert creation_list.index("pytest") == 5


# Тест проверки очистки списка от элементов
def test_null_value(creation_list):
    assert creation_list.clear() == None


# Тест проверки количества элементов в списке
def test_data_count(list_of_data):
    assert len(list_of_data) == 5


# Тест проверки количества элементов в списке после удаления элемента
def test_removal_item_from_list(remove_element):
    assert len(remove_element) == 3


# Тест проверки добавления элемента в список и сравнение его длины
@pytest.mark.parametrize('item', [1, 2, 3])
def test_addition_item_in_list(create_list, item):
    create_list.append(item)
    print(create_list)
    assert item in create_list
