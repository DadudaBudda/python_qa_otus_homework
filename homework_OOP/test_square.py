from homework_OOP.figure import Square


def test_create_square():
    square = Square(a=10)
    assert square.name == 'Square'


def test_square_perimeter():
    square = Square(a=10)
    assert square.find_perimeter() == 40


def test_square_area():
    square = Square(a=10)
    assert square.find_area() == 100


def test_add_areas():
    square = Square(a=10)
    assert square.add_area(square.find_area()) == 200


def test_error():
    square = Square(a=-1)
    assert square.a > 0, 'Должно быть больше нуля'
