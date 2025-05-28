"""              1. Атрибуты классов и статические методы                    """

# Создайте класс Counter, который будет отслеживать количество созданных экземпляров. Используйте атрибут класса.

""" 
class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count) 
"""

class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

    @staticmethod
    def get_count():
        return Counter.count

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.get_count())

# Напишите класс MathUtils со статическими методами add(a, b), multiply(a, b), factorial(n).

class MathUtils:
    def __init__(self):
        pass
    
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

print(MathUtils.add(5, 5))
print(MathUtils.multiply(4, 5))
print(MathUtils.factorial(5))

# Создайте класс User с атрибутом класса total_users = 0, который увеличивается при создании нового пользователя.

class User:
    total_users = 0 

    def __init__(self, username):
        self.username = username
        User.total_users += 1 

user1 = User("Alice")
print(User.total_users)

user2 = User("Bob")
print(User.total_users)

"""                         2. Класс object                     """

# Создайте пустой класс EmptyClass, который наследуется от object. Добавьте в него метод __str__, возвращающий строку "This is an empty class".

class EmptyClass(object):
    def __str__(self):
        return "This is an empty class"
    
empty = EmptyClass()
print(empty)

# Переопределите метод __eq__ в классе Point (с атрибутами x и y), чтобы точки сравнивались по координатам.

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __eq__(self, other):
        if self.x != other.x:
            return False
        if self.y != other.y:
            return False
        return True

point = Point(10, 1)
point1 = Point(1, 10)
point2 = Point(10, 1) 

result = point == point1
print(result)

print(point1 == point2)
print(point == point2)

"""                     3. Строковое представление объекта                       """

# Создайте класс Book с атрибутами title, author и year. Переопределите __str__ и __repr__.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
    
    def __str__(self):
        return f'«{self.title}» — {self.author} ({self.year} г.)'
    
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', year={self.year})"
    
book = Book("Трансерфинг реальности", "Вадим Зеланд", 2004)

print(book)
print(repr(book))

# Напишите класс Student с полями name и grades. Сделайте так, чтобы print(student) выводил имя и средний балл.

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades
    
    def __str__(self):
        return f"{self.name}, средний балл: {sum(self.grades)/len(self.grades)}"


student = Student('Уруру', [5, 3, 4, 3, 5])
print(student)

"""                     4. Перегрузка операторов                 """

# Реализуйте класс Vector с перегрузкой операторов +, -, * (скалярное произведение).

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    
    def __str__(self):
        return f"({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(1, -1)
print(v1 + v2)
print(v1 - v2)
print(v1 * v2)

# Создайте класс Fraction (дробь) с перегрузкой +, -, *, /.



# Перегрузите оператор == для класса Rectangle (сравнивайте площади).

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def __eq__(self, other):
        return self.width * self.height == other.width * other.height


r1 = Rectangle(4, 5)
r2 = Rectangle(2, 10)
r3 = Rectangle(5, 5)

print(r1 == r2)
print(r1 == r3)

"""                         5. Абстрактные классы и методы                       """

# Создайте абстрактный класс Shape с абстрактными методами area() и perimeter(). Реализуйте подклассы Circle и Square.

import abc

class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self): pass
    
    @abc.abstractmethod
    def perimeter(self): pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14159 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    
    def __str__(self):
        return f"Круг с радиусом {self.radius}"


class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    
    def __str__(self):
        return f"Квадрат со стороной {self.side}"


circle = Circle(5)
square = Square(4)

print(circle)
print(square)

# Напишите абстрактный класс Animal с методом make_sound(). Создайте классы Dog и Cat, реализующие этот метод.

import abc

class Animal(abc.ABC):
    @abc.abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Гав-гав!"

class Cat(Animal):
    def make_sound(self):
        return "Мяу!"

dog = Dog()
print(dog.make_sound())

cat = Cat()
print(cat.make_sound())

# Создайте абстрактный класс DatabaseConnector с абстрактными методами connect() и disconnect(). Реализуйте подкласс PostgresConnector.

import abc

class DatabaseConnector(abc.ABC):
    @abc.abstractmethod
    def connect(self):
        pass

    @abc.abstractmethod
    def disconnect(self):
        pass

class PostgresConnector(DatabaseConnector):
    def connect(self):
        print('Подключение ......')

    def disconnect(self):
        print('Отключение ......')

postgres_connector = PostgresConnector()
postgres_connector.connect()
postgres_connector.disconnect()