# def main(inerfunc):
#     def out():
#         print("***")
#         inerfunc()
#         print("***")
#     return out

# @main                                           #   Аннотация(decorators, @decorator) — это специальный синтаксис, который позволяет модифицировать поведение функций или классов, не изменяя их исходный код.
# def myFunc():
#     print("Моя функция а во круг декоратор")
#                                                 #    ***        
# myFunc()                                        #    Моя функция а во круг декоратор 
#                                                 #    ***  
# 
#Зачем нужны декораторы?
# Добавление логирования
# Замер времени выполнения
# Проверка прав доступа
# Кеширование результатов
# Изменение поведения функции без правки её кода


""" 
def check(input_function):
    def output_func(*args):                #   бесконечный приём аргументов
        input_function(*args)              #   Любые аргументы, переданные в print_person(), попадают в *args
    return output_func

@check
def print_person(name, age):
    print(f"{name} {age}")
print_person("Name", 50)             #    Name 50
"""            


""" 
def check(input_function):
    def output_func(*args):          
       name = args[0]
       age = args[1]
       if age < 0: age = 1
       input_function(name, age)
    return output_func

@check
def print_person(name, age):
    print(f"{name} {age}")                                   #   Ururu 1

print_person("Ururu", -9) 
"""


""" 
def check(input_function):
    def output_func(*args):          
       name = args[0]
       age = args[1]
       if age < 0: print("Ururu больше 0 лет")               #   Ururu больше 0 лет
       input_function(name, age)
    return output_func

@check
def print_person(name, age):
    print(f"{name} {age}")                                   #   #   Ururu -9

print_person("Ururu", -9)          
""" 




""" 
class Person:
    def __init__(self, name, age):
        self.name = name  # имя человека
        self.age = age    # возраст человека
        pass 
"""

""" 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def namemetod(self):
        print(f"Мой первый метод на пайтоне. Я студент группы Пайтон 47 {self.name}")

robert = Person("Роберт", "70")            #   70 в ковычках будет строкой
robert.namemetod()                         #   Мой первый метод на пайтоне. Я студент группы Пайтон 47 Роберт """



def process_data(*args):
    print(f"Данные: {args}")

data = [1, 2, 3]
process_data(*data)                #  Данные: (1, 2, 3)



def show_args(*args):
    print(args, type(args))
                                  
show_args(1, 'a', True)           #  (1, 'a', True) <class 'tuple'>     # Кортеж!



def check_args(*args):
    if len(args) == 0:
        print("Нет аргументов!")
    else:
        print(f"Получено {len(args)} аргументов")

check_args(10, 20)  # Получено 2 аргумента



def log_args(func):
    def wrapper(*args):
        print(f"Аргументы: {args} (тип: {type(args)})")
        return func(*args)
    return wrapper

@log_args
def greet(name, age):
    print(f"Привет, {name}! Тебе {age} лет.")
                                        #   Аргументы: ('Анна', 25) (тип: <class 'tuple'>)
greet("Анна", 25)                       #   Привет, Анна! Тебе 25 лет.


