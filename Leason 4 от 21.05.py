"""                                                         Инаксуляция 
"""


""" 
class Person:
    def __init__(self, name, age):
        self.__name = name           # 
        self.__age = age             # 
                 
    def print(self):
        print(f"{self.__name}, {self.__age}")

object1 = Person("Ururu", 16)
object1.print()                 #  Ururu, 16
object1.__age = 33
object1.__name = "Bob"
object1.print()                 #  Ururu, 16 """

"""                                          Нужны методы доступа, чтобы изменить приватный атрибут                                                                           """

""" 
class Person:
    def __init__(self, name, age):
        self.__name = name           #  "private" (приватный) член класса
        self.__age = age             #   Приватный атрибут – доступен только внутри самого класса, скрыт для внешнего доступа

    def get_age(self):
        return self.__age
    def setAge(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимое значение")
                 
    def print(self):
        print(f"{self.__name}, {self.__age}")

object1 = Person("Ururu", 16)
object1.print()                 #  Ururu, 16
object1.setAge(33)
object1.print()                 #  Ururu, 33
 """


""" 
class Person:
    def __init__(self, name, age):
        self.__name = name           
        self.__age = age             
    @property                       #  аннотация
    def age(self):
        return self.__age
    @age.setter                     #
    def age(self, age):
        if 0 < age < 100:
            self.__age = age
        else:
            print("Недопустимое значение")
                 
    def print(self):
        print(f"{self.__name}, {self.__age}")

object1 = Person("Ururu", 16)
 """



"""                             Наследование                                   """
""" 
class Person:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name
    
    def display_info(self):
        print(F"Имя {self.__name}")

class Child(Person):
    def __init__(self, name):
        super().__init__(name)
""" 


""" 
class Father:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes

    def print(self):
        print(F"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

class Mother:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes
    def print(self):
        print(F"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

    def printiqmama(self):
        print(f"{self.iq}")

class Child(Father, Mother):
    def __init__(self, surname, iq, colorEyes, height, colorHair):
        super().__init__(surname, iq, colorEyes)
        self.height = height
        self.colorHair = colorHair

mama = Mother("Фамилия Папы", 120, "Blue")
batya = Father("Фамилия Папы", 100, "Black")
arnold = Child("Фамилия Папы", 150, "BlueBlack", 130, "Цвет волос папы")
arnold.print()
print(arnold)
 """


""" 
class Father:
    def init(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes
    
    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

class Mother:
    def init(self, surname, iqmama, colorEyes):
        self.surname = surname
        self.iqmama = iqmama
        self.colorEyes = colorEyes
    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iqmama}, Цвет глаз = {self.colorEyes}")
    def printiqmama(self):
        print(f"{self.iqmama}")

class Child(Father, Mother):
    def init(self, surname, iq, colorEyes, colorHair):
        super().init(surname, iq, colorEyes)
        self.colorHair = colorHair;

mama = Mother("Фамилия Папа", 120,  "Blue")
batya = Father("Фамилия Папы", 100, "Black")
arnold = Child("Фамилия родителей", 150, "BlueBlack", "Цвет волос папы")
arnold.print()
arnold.printiqmama()
 """



# class Father:
#     def init(self, iqfather):
#         self.iqfather = iqfather
    
#     def printIQFather(self):
#         print(f"{self.iqfather}")

# class Mother:
#     def init(self, colorHair):
#         self.colorHair = colorHair;
#     def printColorHair(self):
#         print(f"МАМА {self.colorHair}")

# class Child(Father, Mother):
#     def init(self, iqfather, colorHair):
#         Father.init(self, iqfather)
#         Mother.init(self, colorHair)




"""                                              Практика/Задачи                                                         """


""" Создай класс "Самолет", объекты будут представлять реальные сущности самолета.
Класс должен отдавать информацию о самолете Марка, модель, год выпуска, мощность, и 
кол-во часов которые он налетал.
Реализуйте программу так, что бы я не смог поменять самые важные данные самолета.
Важность определите самостоятельно. """



# class Plane:
#     def __init__(self, stamp, model, yearOfRelease, power, flightHours):
#         self.__stamp = stamp
#         self.__model = model
#         self.yearOfRelease = yearOfRelease
#         self.__power = power
#         self.flightHours = flightHours

#     def info(self):
#         print(f"Марка самолёта:{self.__stamp} Модель:{self.__model} год выпуска:{self.yearOfRelease} мощность:{self.__power} часов налёта:{self.flightHours}")   

# object1 = Plane( "Airbus", "A320neo", 2013, "20 100 л.с., 666")
# object1.info()

"""        надо было с гетерами сетерами          """




""" 
class Parent:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes
    
    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

class Father(Parent):
    pass

class Mother(Parent):
    pass

class Child:
    def __init__(self, surname, iq_father, colorEyes_father, iq_mother, colorEyes_mother, height, colorHair):
        self.father = Father(surname, iq_father, colorEyes_father)
        self.mother = Mother(surname, iq_mother, colorEyes_mother)
        self.surname = surname
        self.iq = (iq_father + iq_mother) // 2
        self.colorEyes = colorEyes_father
        self.height = height
        self.colorHair = colorHair

    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")
        print(f"Рост: {self.height}, Цвет волос: {self.colorHair}")
        print("--- Данные отца ---")
        self.father.print()
        print("--- Данные матери ---")
        self.mother.print()

child = Child("Иванов", iq_father=120, colorEyes_father="голубые", iq_mother=110, colorEyes_mother="карие", height=175, colorHair="русые")
child.print()
 """


""" 
class Parent:
    def __init__(self, surname, iq, colorEyes):
        self.surname = surname
        self.iq = iq
        self.colorEyes = colorEyes
    
    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")

class Father(Parent):
    def __init__(self, surname, iq, colorEyes):
        super().__init__(surname, iq, colorEyes)

class Mother(Parent):
    def __init__(self, surname, iq, colorEyes):
        super().__init__(surname, iq, colorEyes) 

class Child:
    def __init__(self, surname, iq_father, colorEyes_father, iq_mother, colorEyes_mother, height, colorHair):
        self.father = Father(surname, iq_father, colorEyes_father)
        self.mother = Mother(surname, iq_mother, colorEyes_mother)
        self.surname = surname
        self.iq = (iq_father + iq_mother) // 2
        self.colorEyes = colorEyes_father
        self.height = height
        self.colorHair = colorHair

    def print(self):
        print(f"Фамилия: {self.surname}, IQ = {self.iq}, Цвет глаз = {self.colorEyes}")
        print(f"Рост: {self.height}, Цвет волос: {self.colorHair}")
        print("--- Данные отца ---")
        self.father.print()
        print("--- Данные матери ---")
        self.mother.print()

child = Child("Иванько", iq_father=120, colorEyes_father="голубые", iq_mother=110, colorEyes_mother="карие", height=175, colorHair="русые")
child.print()
 """

