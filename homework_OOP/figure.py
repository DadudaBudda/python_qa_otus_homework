import math


class Figure:

    def __init__(self, name=None, angles=None, perimeter=None, area=None, radius=None):
        self.sum_figures = None
        self.name = name
        self.angles = angles
        self.perimeter = perimeter
        self.area = area
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

    def find_perimeter(self):
        c = math.sqrt(self.a ** 2 + self.b ** 2)
        perimeter = self.a + self.b + c
        return perimeter

    def find_area(self):
        self.area = 0.5 * self.a * self.b
        return self.area


class Rectangle(Figure):

    def __init__(self, a, b):
        super().__init__(name='Rectangle', angles=4)
        self.a = a
        self.b = b
        if a == b:
            raise ValueError('Одна сторона фигуры должна быть больше другой')

    def find_perimeter(self):
        self.perimeter = 2 * self.a + 2 * self.b
        return self.perimeter

    def find_area(self):
        self.area = self.a * self.b
        return self.area


class Square(Figure):

    def __init__(self, a):
        super().__init__(name='Square', angles=4)
        self.a = a

    def find_perimeter(self):
        self.perimeter = 4 * self.a
        return self.perimeter

    def find_area(self):
        self.area = self.a ** 2
        return self.area


class Circle(Figure):

    def __init__(self, radius):
        super().__init__(name='Circle', angles=0)
        self.radius = radius

    def find_perimeter(self):
        self.perimeter = self.radius * 2 * math.pi
        return self.perimeter

    def find_area(self):
        self.area = self.radius ** 2 * math.pi
        return self.area
