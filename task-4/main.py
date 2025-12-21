from abc import ABC, abstractmethod


class Person:

    def __init__(self, first_name: str, last_name: str, age: int):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    def info(self) -> None:
        print(f"ФИО: {self.name}")
        print(f"Возраст: {self.age} лет")


class Student(Person):

    def __init__(self, first_name: str, last_name: str, age: int, group_number: str, average_grade: float):
        super().__init__(first_name, last_name, age)
        self.group_number = group_number
        self.average_grade = average_grade
        self._validate_grade()

    def _validate_grade(self) -> None:
        if not (0 <= self.average_grade <= 5):
            raise ValueError("Средняя оценка должна быть в диапазоне от 0 до 5")

    def calculate_scholarship(self) -> int:
        if self.average_grade == 5:
            return 6000
        elif self.average_grade >= 4:
            return 4000
        else:
            return 0

    def print_scholarship(self) -> None:
        scholarship = self.calculate_scholarship()
        print(f"Размер стипендии: {scholarship} руб.")

    def compare_scholarship(self, other: 'Student') -> str:
        if not isinstance(other, (Student, GraduateStudent)):
            raise ValueError("Можно сравнивать только с объектами Student или GraduateStudent")

        self_scholarship = self.calculate_scholarship()
        other_scholarship = other.calculate_scholarship()

        if self_scholarship > other_scholarship:
            return f"Стипендия {self.name} больше, чем у {other.name}"
        elif self_scholarship < other_scholarship:
            return f"Стипендия {self.name} меньше, чем у {other.name}"
        else:
            return f"Стипендии {self.name} и {other.name} равны"


class GraduateStudent(Student):

    def __init__(self, first_name: str, last_name: str, age: int, group_number: str,
                 average_grade: float, research_work: str):
        super().__init__(first_name, last_name, age, group_number, average_grade)
        self.research_work = research_work

    def calculate_scholarship(self) -> int:
        if self.average_grade == 5:
            return 8000
        elif self.average_grade >= 4:
            return 6000
        else:
            return 0

    def print_info(self) -> None:
        super().print_info()
        print(f"Научная работа: {self.research_work}")
        print(f"Группа: {self.group_number}")
        print(f"Средний балл: {self.average_grade}")


if __name__ == "__main__":

    student1 = Student("Иван", "Иванов", 20, "5132704/50001", 4.8)
    student2 = Student("Мария", "Петрова", 19, "5132704/50002", 3.9)
    graduate = GraduateStudent("Пётр", "Петров", 25, "5132704/50801", 5.0, "Исследование методов машинного обучения")

    print("\nСтудент 1:")
    student1.info()
    student1.print_scholarship()

    print("\nСтудент 2:")
    student2.info()
    student2.print_scholarship()

    print("\nАспирант:")
    graduate.info()
    graduate.print_scholarship()

    print(student1.compare_scholarship(graduate))