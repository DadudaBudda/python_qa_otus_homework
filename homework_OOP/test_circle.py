from homework_OOP.figure import Circle, Triangle


def test_create_circle():
    circle = Circle(radius=5)
    assert circle.name == 'Circle',f'Название фигуры {circle.name}'


def test_circle_perimeter():
    circle = Circle(radius=12)
    assert int(circle.find_perimeter()) == 75, f'Периметр круга не равен 75. Значение {circle.find_perimeter()}'


def test_circle_area():
    circle = Circle(radius=7)
    assert int(circle.find_area()) == 153, f'Площадь круга не равен 153. Значение {circle.find_area()}'


def test_add_areas():
    circle = Circle(radius=2)
    triangle = Triangle(a=12, b=7)
    circle.find_area()
    assert circle.add_area(triangle.find_area()) == 54, f'Площадь двух фигур не равна 54. Значение {circle.add_area(triangle.find_area())} '


def test_error():
    circle = Circle(radius=0)
    assert int(circle.find_area()) != 0, f'Площадь круга не равна 0. Значение {circle.find_area()}'
