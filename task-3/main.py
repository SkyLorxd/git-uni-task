from abc import ABC, abstractmethod
from math import pi, sqrt


class Figure(ABC):
    def __init__(self):
        self._area: float = 0.0
        self._perimeter: float = 0.0

    @property
    def area(self) -> float:
        if not self._area:
            self._area = self.calculate_area()
        return self._area

    @property
    def perimeter(self) -> float:
        if not self._perimeter:
            self._perimeter = self.calculate_perimeter()
        return self._perimeter

    @abstractmethod
    def calculate_area(self) -> float:
        pass

    @abstractmethod
    def calculate_perimeter(self) -> float:
        pass

    def compare_area(self, other: "Figure") -> str:
        if not isinstance(other, Figure):
            raise ValueError("Можно сравнивать только с объектами Figure")

        if self.area > other.area:
            return "Площадь больше"
        elif self.area < other.area:
            return "Площадь меньше"
        else:
            return "Площади равны"

    def compare_perimeter(self, other: "Figure") -> str:
        if not isinstance(other, Figure):
            raise ValueError("Можно сравнивать только с объектами Figure")

        if self.perimeter > other.perimeter:
            return "Периметр больше"
        elif self.perimeter < other.perimeter:
            return "Периметр меньше"
        else:
            return "Периметры равны"


class Rectangle(Figure):
    def __init__(self, length: float, width: float):
        super().__init__()
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_perimeter(self) -> float:
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)


class Circle(Figure):
    def __init__(self, radius: float):
        super().__init__()
        self.radius = radius

    def calculate_area(self) -> float:
        return pi * self.radius ** 2

    def calculate_perimeter(self) -> float:
        return 2 * pi * self.radius


class Triangle(Figure):
    def __init__(self, side_a: float, side_b: float, side_c: float):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

        self._validate_triangle()

    def _validate_triangle(self) -> None:
        sides = [self.side_a, self.side_b, self.side_c]
        if any(side <= 0 for side in sides):
            raise ValueError("Все стороны треугольника должны быть положительными")

        if (self.side_a + self.side_b <= self.side_c or
                self.side_a + self.side_c <= self.side_b or
                self.side_b + self.side_c <= self.side_a):
            raise ValueError("Треугольник с такими сторонами не существует")

    def calculate_area(self) -> float:
        half_perimeter = self.perimeter / 2
        return sqrt(half_perimeter * (half_perimeter - self.side_a) * (half_perimeter - self.side_b) * (half_perimeter - self.side_c))

    def calculate_perimeter(self) -> float:
        return self.side_a + self.side_b + self.side_c


if __name__ == "__main__":
    rectangle = Rectangle(5, 3)
    square = Square(4)
    circle = Circle(3)
    triangle = Triangle(3, 4, 5)

    figures = [rectangle, square, circle, triangle]

    for figure in figures:
        print(f"{figure.__class__.__name__}:")
        print(f"  Площадь: {figure.area:.2f}")
        print(f"  Периметр: {figure.perimeter:.2f}")
        print()

    # Сравнение фигур
    print(f"Сравнение прямоугольника и круга: {rectangle.compare_area(circle)}")
    print(f"Сравнение квадрата и треугольника: {square.compare_perimeter(triangle)}")

