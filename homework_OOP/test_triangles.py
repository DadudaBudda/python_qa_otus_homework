from homework_OOP.figure import Triangle


def test_create_triangle():
    triangle = Triangle(a=10, b=12)
    assert triangle.name == 'Triangle'


def test_triangle_perimeter():
    triangle = Triangle(a=5, b=6)
    assert int(triangle.find_perimeter()) == 18


def test_triangle_area():
    triangle = Triangle(a=5, b=6)
    assert triangle.find_area() == 15


def test_add_areas():
    triangle = Triangle(a=5, b=6)
    assert triangle.add_area(triangle.find_area()) == 30


def test_error():
    triangle = Triangle(a=1, b=-10)
    assert triangle.area < 0, 'Должно быть больше нуля'
