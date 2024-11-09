class Figure():
    def __init__(self):
       pass
    def area_figure(self):
        raise NotImplementedError('Расчет площади не выполнен')
    def perimetr_figure(self):
        raise NotImplementedError('Расчет периметра не выполнен')

class Two_dimenFigure(Figure):
    def __init__(self, height, width):
        super().__init__()
        self.height = height
        self.width = width
    def area_figure(self):
        return self.height * self.width
    def perimetr_figure(self):
        return (self.height + self.width) * 2

class Three_dimenFigure(Figure):
    def __init__(self, height, width, depth):
        super().__init__()
        self.height = height
        self.width = width
        self.depth = depth
    def area_figure(self):
        return 2 * (self.height * self.width + self.width * self.depth + self.height * self.depth)
    def perimetr_figure(self):
        return 4 * (self.height + self.width + self.depth)

class Circle(Two_dimenFigure):
    def __init__(self, radius):
        super().__init__(radius, radius)
        self.radius = radius
        self.pi = 3.14

    def area_figure(self):
        return self.pi * (self.radius ** 2)
    def perimetr_figure(self):
        return 2 * self.pi * self.radius

class Rectangle(Two_dimenFigure):
    def __init__(self, height, width):
        super().__init__(height, width)


class Sphere(Three_dimenFigure):
    def __init__(self, radius):
        super().__init__(radius, radius, radius)
        self.radius = radius
        self.pi = 3.14

    def area_figure(self):
        return 4 * self.pi * (self.radius**2)
    def perimetr_figure(self):
        return 2 * self.pi * self.radius

class Cube(Three_dimenFigure):
    def __init__(self, side):
        super().__init__(side, side, side)
        self.side = side

    def area_figure(self):
        return 6 * (self.side ** 2)
    def perimetr_figure(self):
        return 12 * self.side

circle = Circle(radius=5)
rectangle = Rectangle(width=4, height=6)
sphere = Sphere(radius=3)
cube = Cube(side=0)

print(circle.area_figure())
print(rectangle.perimetr_figure())
print(sphere.area_figure())
print(cube.perimetr_figure())



