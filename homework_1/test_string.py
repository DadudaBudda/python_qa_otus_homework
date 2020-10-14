import pytest


# Тест проверки длины фразы
def test_length_of_phrase(сreate_text):
    print(len(сreate_text))


# Тест проверки корректности сложения двух частей фразы в одну
def test_concatenation_phrase(сoncatenate_text):
    print(сoncatenate_text)
    assert сoncatenate_text == "Pytest - тестовый фреймворк"


# Тест сравнения типов данных фраз
@pytest.mark.parametrize('text', ["Pytest - тестовый фреймворк"])
def test_comparison_types(сreate_text, text):
    assert type(сreate_text) == type(text)


# Тест корректности среза фразы
def test_trimming_phrase(сreate_text):
    assert сreate_text[:6] == "Pytest"


# Тест положения регистра фразы
def test_upper_case(сreate_text):
    assert сreate_text.upper() == "PYTEST - ТЕСТОВЫЙ ФРЕЙМВОРК"
