import pytest


# Тест проверки добавления элемента во множество
@pytest.mark.parametrize('items', {"Tom", "Bob", "Alice"})
def test_addition_item_in_list(create_set, items):
    create_set.add(items)
    print(create_set)
    assert items in create_set


# Тест удаления элемента из множества
@pytest.mark.parametrize('items', {"Mike", "Bill", "Ted"})
def test_deletion_element(create_set, items):
    create_set.remove(items)
    print(create_set)
    assert not items in create_set


# Тест удаления всех элементов из множества
def test_deletion_elements(create_set):
    create_set.clear()
    assert len(create_set) == 0


# Тест сравнения элементов множеств
@pytest.mark.parametrize('items', {"Mike", "Bill", "Ted"})
def test_comparison_elements(create_frozen_set, items):
    create_frozen_set.issubset(items)
    print(create_frozen_set)
    assert items in create_frozen_set


# Тест проверки корректности добавления элемента во множество
def test_unique_set(add_unique_value):
    assert len(add_unique_value) == 6
