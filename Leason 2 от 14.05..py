""" Оператор return и возвращение результата из функции
 """
# def print_abountme(name):
#     print("Меня зовут:", name)
# print_abountme('Ururu')     #  Меня зовут: Ururu

# def print_abountme(name, age = 18):
#     print("Меня зовут:", name, age)
# print_abountme('Ururu')     #  Меня зовут: Ururu 18

# def print_abountme(name, age = 18):
#     print("Меня зовут:", name, age)
# print_abountme(age =16, name = "Ururu")    #  Меня зовут: Ururu 16

# def print_abountme(name, age,*, city, city1):    #   * означает что можно только так передать все последующие параметры аргумента city = 'Sochi'
#     print("Меня зовут:", name, age, city)
# print_abountme("Ururu", "Age", city = 'Sochi', city1 = 'Sochi1')    #  Ururu Age Sochi Sochi1



# def sum(*numbers):
#     result = 0
#     for j in numbers:
#         result += j
#     print(f"sum = {result}")    

# def get_info():
#     return "My Info"
# print(get_info())


# def speed_limited(speed):
#     if speed > 150:
#         print("Вы нарушаете, пока")
#         return
#     else:
#         print("Всё ок")
# speed_limited(200)         #  Вы нарушаете, пока


# def say_hello(): print("Hello")
# def say_goodbye(): print("Goodbye")

# message = say_hello
# message()                #  Hello


# def math_operation(a, b, operation):
#     result = operation(a, b)
#     print(f"result = {result}")

# def sum(a,b): return a + b
# def multiply(a, b): return a * b

# math_operation(555, 111, sum)    #  666
# math_operation(12,2, multiply)   #  24


""" def sum (a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def select(choice):
    if choice == 1:
        return sum
    elif choice == 2:
        return subtract
    else:
        return multiply
    
oper1 = select(1)
print(oper1(1,2))    #  3

oper2 = select(2)
print(oper2(4,4))    #  0

oper3 = select(3)
print(oper3(2,2))    #  4 """


""" Лямбда-выражения """

# square = lambda n: n * n
# print(square(4))     #  16
# print(square(5))     #  25

# def kvadrat(n):
#     return n * n
# print(kvadrat(4))    #  16


# square = lambda n,p: n * p
# print(square(4,4))     #  16
# print(square(5,5))     #  25

# def kvadrat(n):
#     return n * n
# print(kvadrat(4))    #  16


""" def select(choice):
    if choice == 1:
        return lambda a,b: a + b
    elif choice == 2:
        return lambda a,b: a - b
    else:
        return lambda a,b: a * b
    
oper1 = select(1)
print(oper1(1,2))    #  3 """



""" Преобразование типов """

# number1 = 60
# number2 = 12.5
# result = number1 + number2
# print(result)               #  72.5
# print(type(result))         #  <class 'float'>2


# a = '2'
# b = 2
# c = int(a) + b

""" # Global variable
globalvar = "Myname"
def test():
# Local variable
    word = "Word"
    print("Hello World", word)    # ?

def test2():
    print("!Hello World")

print(word) """



""" secret = 123

def test2():
    # global secret  # переводит в глобальную переменную                       
    secret = 1234                                                #  ?
    print("Секретная переменная:", secret)
test2()
print(secret)   #  123 """



"""                                              Вложенность                                             """

""" def outher():
    n = 5  #  Лексическое окружение

    def inner():
        nonlocal n
        n = 25                                                #  изучить
        print(n)

    inner()
    # print(n)      #  print(n)
outher()        #   25 """



# def outher():           #  Внешняя функция
#     n = 5               #  Лексическое окружение

#     def inner():        #  Локальная функция
#         nonlocal n 
#         n += 1          #  Операция с лесическим окружением
#         print(n)
#     return inner
# """                                                     Замыкание          """
# plus = outher()
# # 
# plus()
# plus()
# plus()


""" Задача: Напишите функцию createCounter(), которая возвращает другую функцию. Возвращаемая функция при каждом вызове должна увеличивать счетчик и возвращать его текущее значение. """


""" def createCounter():
    n = 0

    def counter():
        nonlocal n    # nonlocal позволяет изменять переменную из ближайшей внешней (но не глобальной) области видимости.
        n += 1
        return n
    return createCounter1
createCounter1 = createCounter()
print(createCounter1())
print(createCounter1())
print(createCounter1())
 """

# def createCounter():
#     n = 0

#     def counter():
#         nonlocal n
#         n += 1
#         return n
#     return createCounter1
# createCounter1 = createCounter()
# createCounter1()
# createCounter1()
# createCounter1()


secret = 123  # Глобальная переменная

def test2():
    # global secret  # закомментировано
    secret = 1234    # Локальная переменная функции
    print("Секретная переменная внутри функции:", secret)

test2()
print("Глобальная переменная:", secret)  # 123

count = 0  # Глобальная переменная

if True:
    temp = 10  # Локальная переменная (временная, существует только в блоке if)
    count += temp  # Увеличиваем глобальную count на значение локальной temp
    print(temp)  # Выводит 10 (локальная temp доступна внутри блока)

print(count)  # Выводит 10 (глобальная count была изменена)

# Попытка вывести temp здесь вызовет ошибку!
print(temp)  # NameError: name 'temp' is not defined


