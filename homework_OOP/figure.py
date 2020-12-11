import math


class Figure:

    def __init__(self, name=None, angles=None, perimeter=None, area=None, radius=None):
        self.sum_figures = None
        self.name = name
        self.angles = angles

        self.radius = radius

    def get_name(self):
        return self.name

    def get_angles(self):
        return self.angles

    def add_area(self, another_figure):
        self.sum_figures = int(self.area + another_figure)
        return self.sum_figures


class Triangle(Figure):

    def __init__(self, a, b):
        super().__init__(name='Triangle', angles=3)
        self.a = a
        self.b = b

    @property
    def find_perimeter(self):
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        perimeter = self.a + self.b + c
        return int(perimeter)

    @property
    def find_area(self):
        area = 0.5 * self.a * self.b
        return int(area)


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__(name='Rectangle', angles=4)
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('Одна сторона фигуры должна быть больше другой')

    @property
    def find_perimeter(self):
        perimeter = 2 * self.a + 2 * self.b
        return int(perimeter)

    @property
    def find_area(self):
        area = self.a * self.b
        return int(area)


class Square(Figure):

    def __init__(self, a):
        super().__init__(name='Square', angles=4)
        self.a = a

    @property
    def find_perimeter(self):
        perimeter = 4 * self.a
        return int(perimeter)

    @property
    def find_area(self):
        area = self.a ** 2
        return int(area)


class Circle(Figure):

    def __init__(self, radius):
        super().__init__(name='Circle', angles=0)
        self.radius = radius

    @property
    def find_perimeter(self):
        perimeter = self.radius * 2 * math.pi
        return int(perimeter)

    @property
    def find_area(self):
        area = self.radius ** 2 * math.pi
        return int(area)
