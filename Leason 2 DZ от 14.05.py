
""" 1. Параметры функции
Задача: Напишите функцию, которая принимает три обязательных
параметра и два необязательных, затем возвращает их сумму. """

def sum (a,b,c,d=2,e=5):
    return a+b+c+d+e
print(sum(1,2,3,))
print(sum(2,2,2,2,2))


""" 2. Оператор return и возвращение результата
Задача: Создайте функцию, которая проверяет, является ли число
четным, и возвращает True или False. """

def check_even(number):
    return number % 2 == 0
print(check_even(4))
print(check_even(5))


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
print(is_even(4))
print(is_even(5))


numbers = [1, 2, 3, 4, 5]
labels = ["чётное" if x % 2 == 0 else "нечётное" for x in numbers]
print(labels) 


""" 3. Функция как тип, параметр и результат другой функции
Задача: Напишите функцию, которая принимает другую функцию и
список чисел, применяет эту функцию к каждому элементу списка. """

def outer(func, list):
    for i in list:
        print(func(i))

def inner(i):
    return 1 + i

list1 = [1, 5, 3]
outer(inner, list1)


def outer(numbers):
    def inner(i):
        return 1 + i

    for num in numbers:
        print(inner(num))

list1 = [1, 5, 3]
outer(list1)
      

result = list(map(lambda x: x + 10, [1, 2, 3]))  #map (возвращает итератор, который можно преобразовать в список)
print(result)


numbers1 = [1, 2, 3, 4]
doubled = map(lambda x: x * 2, numbers1)
print(list(doubled)) #Функция list() в Python создаёт пустой список или преобразует другой объект в список.Она принимает любую итерацию (объект, который можно перебирать) в качестве параметра и возвращает список.


result1 = [x + 10 for x in [1, 2, 3]]
print(result1)


""" 4. Область видимости переменных
Объявите глобальную переменную count и установите её значение в 0.
Внутри блока if True: создайте локальную переменную temp со
значением 10.
Увеличьте значение count на значение temp.
Выведите temp внутри блока — должно работать.
Выведите count вне блока — должно работать.
Попробуйте вывести temp вне блока — должна возникнуть ошибка,
так как temp локальная. """

count = 0

if True:                  #  `if` не создаёт новой области видимости
    temp = 10
    count += temp
    print(temp)
print(temp)       # не выводит ошибки так как не функция, которая могла бы создать локальную область видимости(переменные внутри функции не видны снаружи, если не объявлены как global или nonlocal).
print(count) # во всех  случаях выводит 10

def local():
    temp=5
    temp+=count
    return print(temp)
local()
print(temp)


""" 5. Простой счётчик
Создать замыкание, которое возвращает функцию-счётчик,
увеличивающую значение на 1 при каждом вызове. """

def createCounter():
    n = 0

    def counter():
        nonlocal n  # nonlocal позволяет изменять переменную из ближайшей внешней (но не глобальной) области видимости.
        n += 1
        return n
    return counter

counter = createCounter()
print(counter())
print(counter())
print(counter())


""" 6. Счётчик с шагом
Модифицируйте счетчик так, чтобы он увеличивал значение не на 1, а
на заданный шаг. """

def create_counter(step=1):
    count = 0
    def counter():
        nonlocal count
        count += step
        return count
    return counter

counter1 = create_counter()
print(counter1())
print(counter1())
print(counter1())

counter2 = create_counter(3)
print(counter2())
print(counter2())
print(counter2())

counter3 = create_counter(-2)
print(counter3())
print(counter3())
print(counter1())