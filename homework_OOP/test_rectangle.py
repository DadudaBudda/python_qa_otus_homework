import pytest

from homework_OOP.figure import Rectangle


@pytest.mark.parametrize('a, b', [(1, 2), (5, 6), (10, 10)])
def test_create_rectangle_with_valid_values(a, b):
    if a > b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a < b:
        rectangle = Rectangle(a, b)
        assert rectangle.name == 'Rectangle'
    elif a == b:
        pytest.raises(ValueError)


def test_rectangle_perimeter():
    rectangle = Rectangle(a=6, b=5)
    assert rectangle.find_perimeter() == 22, f'Периметр не равна 22. Значение {rectangle.find_perimeter()}'


def test_rectangle_area():
    rectangle = Rectangle(a=6, b=5)
    assert rectangle.find_area() == 30, f'Площадь не равна 30. Значение {rectangle.find_area()}'


def test_add_areas():
    rectangle = Rectangle(a=6, b=5)
    assert rectangle.add_area(rectangle.find_area()) == 60, f'Площадь двух фигур не равна 60.\
     Значение {rectangle.add_area(rectangle.find_area())}'


def test_error():
    rectangle = Rectangle(a=6, b=6)
    assert rectangle.a != rectangle.b, 'Одна сторона фигуры должна быть больше другой'

