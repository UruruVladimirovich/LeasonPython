"""                                                               СТАТИЧЕСКИЙ АТРИБУТ                                   """
""" 
class Person:
    type = "Person"              #  Атрибуты класса
    nationality = "Russian"
print(Person.type)               #  Person
print(Person.nationality)        #  Russian 
"""

""" 
class Person:
    type = "Person"              #  Атрибуты класса
    nationality = "Russian"

    def __init__(self, name):
        self.name = name

# person1 = Person("Имя человек")
# print(person1.type)              #  Person
# print(person1.nationality)       #  Russian 
Person.type = "Изменить значение статического атрибута"

print(Person.type)        #   Изменить значение статического атрибута
 """

""" 
class Person:
    default_name = "Undefined"                   #  СТАТИЧЕСКИЙ АТРИБУТ

    def __init__(self, name):
        if name:
            self.name = name
        else:
            self.name = Person.default_name

person1 = Person("Имя")
person2 = Person("")
print(person1.name)             #   Имя
print(person2.name)             #   Undefined
 """

""" 
#  Статические методы
class Person:
    __type = "Person"

    @staticmethod
    def print():
        print(Person.__type)

person1 = Person()
person1.print()                    #   Person
 """

""" 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name{self.name}")

    def __str__(self):                                #  метод возращает строку
        return f"Name: {self.name}, {self.age}"
person1 = Person("Имя", 12)                       #  Name: Имя, 12
print(person1)     #  строковое представление
 """


# class Counter:
#     def __init__(self, value):
#         self.value = value
#     def __add__(self, other):
#         return Counter(self.value + other.value)

# counter1 = Counter(50)
# counter2 = Counter(10)
# counter3 = counter1 + counter2
# print(counter3.value)                 #   60


""" 
class Counter:
    def __init__(self, value):
        self.value = value
    def __bool__(self):
        return self.value > 0

def check(counter):
    if counter: print("Counter == True")
    else: print("Counter == False")

counter1 = Counter(3)
check(counter1)           #  Counter == True

counter2 = Counter(-11)
check(counter2)           #  Counter == False
 """



""" 
Создайте класс Vector, который представляет вектор и определите в нем операторы сложения и вычитания. 
Для сложения векторо применяется формула a + b = {ax + bx; ay + by}, а для вычитания a - b = {ax - bx; ay - by} 
"""

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __add__(self, other):  # Для оператора +
#         return Vector(self.x + other.x, self.y + other.y)

#     def __sub__(self, other):  # Для оператора -
#         return Vector(self.x - other.x, self.y - other.y)
# # Создаем векторы
# vect1 = Vector(10, 300)
# vect2 = Vector(200, 100)

# result = vect1 + vect2
# print(f"Сложение: x = {result.x}, y = {result.y}")  # x = 210, y = 400

# result = vect1 - vect2
# print(f"Вычитание: x = {result.x}, y = {result.y}")  # x = -190, y = 200


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __str__(self):
        return f"({self.x}, {self.y})"

a = Vector(2, 3)
b = Vector(1, -1)

print("a + b = (ax + bx; ay + by)", a + b)
print("a - b = (ax - bx; ay - by)", a - b)


""" 
                                                Абстрактные методы
"""

""" 
import abc                                   #  подключаем библиотеку
class Shape (abc.ABC):
    @abc.abstractmethod
    def area (self): pass

class Rectangle(Shape):
    def __init__(self, width, heigth):
        self.width = width
        self.heigth = heigth
    def area(self): return self.width * self.heigth

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self): return self.radius * self.radius * 3.14

def displayArea(shape):
    print("Area: ", shape.area())

rect = Rectangle(150, 40)
circ = Circle(90)
displayArea(rect)                  #    6000
displayArea(circ)                  #    25434.0
 """


""" 
                                                                    Практическое задание
"""
# 1 Квадрат
# 2 Ромб
# 3 Трапеция
# 4 Пятиугольник
# 5 Треугольник
# 6 Сфера

# import abc                                   #  подключаем библиотеку
# class Shape (abc.ABC):
#     @abc.abstractmethod
#     def area (self): pass

# class Square(Shape):
#     def __init__(self, width, heigth):
#         self.width = width
#         self.heigth = heigth
#     def area(self): return self.width * self.heigth

# class Rhomb(Shape):
#     def __init__(self, d1, d2):
#         self.d1 = d1
#         self.d2 = d2
#     def area(self): return self.width * self.heigth

# class Trapezoid(Shape):
#     def __init__(self, a, b, height1):
#         self.a = a
#         self.b = b
#         self.height1 = height1
#     def area(self): return (self.a + self.b) * self.height1 / 2

# class Pentagon(Shape):
#     def __init__(self, c, d):
#         self.c = c
#         self.d = d
#     def area(self): return (self.c*self.d*0.5)*5           #    не доделанно


"""                                                 Проверка на ошибки                                         """
try:     
    value = int(input("Введение значение, что бы пребразовать его в целое число"))
    print(f"Введите число пользователя", value)
except:
    print("Преоброзование не успеешно")