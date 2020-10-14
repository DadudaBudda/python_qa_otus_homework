import pytest


# Тест проверки длины словаря
def test_dictionary_length(creation_dictionary):
    assert len(creation_dictionary) == 3


# Тест сравнения заданных ключей в словаре
@pytest.mark.parametrize('key', [1, 2, '3'])
def test_count_of_keys(creation_dictionary, key):
    assert key in creation_dictionary.keys()


# Тест сравнения копии и оригинала словаря
def test_copy_comparison(creation_dictionary):
    new_dictionary = creation_dictionary.copy()
    assert new_dictionary == creation_dictionary


# Тест добавления ключа-значения в словарь
def test_addition_item(creation_dictionary):
    first_dictionary = creation_dictionary.copy()
    second_dictionary = creation_dictionary.setdefault(20, 0)
    assert first_dictionary != second_dictionary


# Тест удаления заданных ключей из словаря
@pytest.mark.parametrize('key', [1, ])
def test_deletion_key_in_dictionary(creation_dictionary, key):
    creation_dictionary.pop(key)
    assert key not in creation_dictionary
