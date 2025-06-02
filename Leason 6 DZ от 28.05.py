"""                         Методы списков (list)                       """


"""                         # append(x) – Добавление элемента(добавляет элемент x в конец списка.)
lst = [1, 2]
lst.append(3)               # [1, 2, 3]
"""


"""                         # extend(iterable) – Расширение списка(расширяет список, добавляя элементы из итерируемого объекта (списка, кортежа, строки и т. д.).)
lst = [1, 2]
lst.extend([3, 4])          # [1, 2, 3, 4]
"""


"""                         # insert(i, x)  –  Вставка элемента(вставляет элемент x на позицию i.)
lst = [1, 3]
lst.insert(1, 2)            # [1, 2, 3]

fruits = ['яблоко', 'банан', 'апельсин']
fruits.insert(1, 'груша')   # Вставляем 'груша' на позицию 1 (второе место)
print(fruits)               # ['яблоко', 'груша', 'банан', 'апельсин']
"""


"""                         # remove(x) – Удаление элемента(удаляет первое вхождение элемента x (вызывает ошибку, если элемента нет).)
lst = [1, 2, 2, 3]
lst.remove(2)               # [1, 2, 3]

numbers = [10, 20, 30, 20, 40]
numbers.remove(20)          # Удаляет только первую 20
print(numbers)              # [10, 30, 20, 40]
"""


"""                         # pop([i]) – Удаление с возвратом(удаляет и возвращает элемент на позиции i (по умолчанию — последний).)
lst = [1, 2, 3]
last = lst.pop()            # last = 3, lst = [1, 2]
second = lst.pop(1)         # second = 2, lst = [1]

lst = [1, 2, 3]
x = lst.pop(1)              # x = 2, lst = [1, 3]
"""


"""                         # clear() – полностью очищает список.
lst = [1, 2, 3]
lst.clear()                 # []
"""


"""                         # index(x[, start[, end]]) – возвращает индекс первого вхождения x (можно указать диапазон start:end).
lst = [10, 20, 30, 20]
idx = lst.index(20)         # 1

lst = [10, 20, 30, 20, 40, 20]
idx = lst.index(20, 2, 5)   # Ищем 20 между индексами 2 и 5
print(idx)                  # Вывод: 3 (первое вхождение после индекса 2)
"""


"""                         # count(x) – возвращает количество вхождений элемента x.
lst = [1, 2, 2, 3]
c = lst.count(2)            # 2

numbers = [1, 2, 3, 2, 4, 2, 5]
count_two = numbers.count(2)
print(count_two)            # Вывод: 3 (число 2 встречается 3 раза)
"""


"""                         # sort(key=None, reverse=False) – сортирует список (можно задать ключ key и порядок reverse).
lst = [3, 1, 4, 2]
lst.sort()                  # [1, 2, 3, 4]

words = ["Python", "is", "awesome", "!"]
words.sort(key=len)         # Сортировка по длине слова
print(words)                # ['!', 'is', 'Python', 'awesome']
"""


"""                         # reverse() – разворачивает список в обратном порядке.
lst = [1, 2, 3]
lst.reverse()               # [3, 2, 1]
"""


"""                         # copy() – создает поверхностную копию списка.
lst = [1, 2, 3]
lst2 = lst.copy()           # [1, 2, 3] (новая ссылка)
"""


"""                         # + – конкатенация списков
lst = [1, 2] + [3, 4]       # [1, 2, 3, 4]
"""


"""                         # * – повторение списка
lst = [0] * 3               # [0, 0, 0]
"""


"""                         # del – удаление элемента по индексу
lst = [1, 2, 3]
del lst[1]                  # [1, 3]
"""


"""                         # list(iterable) — преобразует любой итерируемый объект в список
text = "hello"
chars = list(text)  
print(chars)                # ['h', 'e', 'l', 'l', 'o']
"""


"""                         # len(list) — длина списка
lst = [10, 20, 30]
print(len(lst))             # 3
"""


"""                         # sorted(list, key=None, reverse=False) — возвращает новый отсортированный список
numbers = [3, 1, 4, 2]
sorted_numbers = sorted(numbers)  # [1, 2, 3, 4]
print(numbers)              # [3, 1, 4, 2] (исходный список не изменился)
"""


"""                         # min(list) / max(list) — минимальный и максимальный элементы
lst = [5, 2, 8, 1]
print(min(lst))             # 1
print(max(lst))             # 8
"""


"""                         # sum(list) — сумма элементов (только для чисел!)
numbers = [1, 2, 3, 4]
print(sum(numbers))         # 10
"""


"""                         # any(list) — True, если хотя бы один элемент True (или не пустой)
lst = [False, 0, "", None, 5]
print(any(lst))             # True (потому что 5 — True)
"""


"""                         # all(list) — True, если все элементы True (или не пустые)
lst = [1, 2, 3, 0]
print(all(lst))             # False (потому что 0 — False)
"""


"""                         # enumerate(list) — возвращает пары (индекс, элемент)
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(i, fruit)         # 0 apple, 1 banana, 2 cherry
"""


"""                         # zip(list1, list2, ...) — объединяет списки попарно
names = ["Alice", "Bob"]
ages = [25, 30]
zipped = zip(names, ages)   # [('Alice', 25), ('Bob', 30)]
print(list(zipped)) 
"""


"""                         # filter(function, list) — фильтрует элементы по условию
numbers = [1, 2, 3, 4, 5]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))           # [2, 4] 
"""


"""                         # map(function, list) — применяет функцию к каждому элементу
numbers = [1, 2, 3]
squared = map(lambda x: x ** 2, numbers)
print(list(squared))        # [1, 4, 9] 

numbers = [1, 2, 3]
squared = list(map(lambda x: x ** 2, numbers))  # Сразу преобразуем в список
print(squared)              # [1, 4, 9]
"""
numbers = [1, 2, 3, 4, 5]
squared_evens = map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers))
print(list(squared_evens))  # [4, 16]  (2² и 4²)




"""                                 Кортежи                              """

                                # Простой кортеж
""" 
my_tuple = (1, 2, 3)
print(my_tuple)                 # (1, 2, 3) 
"""

                                # Кортеж из одного элемента (нужна запятая!)
""" 
single_tuple = (42,)            # Без запятой Python воспримет это как число, а не кортеж
print(single_tuple)             # (42,) 
"""

                                # Кортеж без скобок (автоматически упаковывается)
""" 
auto_tuple = 10, 20, 30
print(auto_tuple)               # (10, 20, 30) 
"""

                                # Кортеж с разными типами данных
""" 
mixed_tuple = ("apple", 3.14, True, 42)
print(mixed_tuple)              # ('apple', 3.14, True, 42) 
"""

                                # Кортеж из списка (преобразование)
""" 
my_list = [5, 6, 7]
tuple_from_list = tuple(my_list)
print(tuple_from_list)          # (5, 6, 7) 
"""

                                # Распаковка кортежа
""" 
coordinates = (10, 20, 30)
x, y, z = coordinates
print(x, y, z)                  # 10 20 30 
"""

                                # Использование в функциях (возврат нескольких значений)
""" 
def get_user():
    return "Alice", 25, "alice@example.com"

name, age, email = get_user()
print(name, age, email)         # Alice 25 alice@example.com 
"""

                                # Кортеж как ключ словаря (т.к. он неизменяемый)
""" 
locations = {
    (35.68, 139.76): "Tokyo",
    (40.71, -74.01): "New York"
}
print(locations[(35.68, 139.76)])  # Tokyo 
"""

                                # Срезы в кортежах
""" 
numbers = (0, 1, 2, 3, 4, 5)
print(numbers[1:4])             # (1, 2, 3) 
"""