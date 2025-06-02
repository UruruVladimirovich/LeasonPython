#  List(список)
# number = [1, 2, 3, 4, 5, 6, "Name", True, False]
# print(number)                                 #   [1, 2, 3, 4, 5, 6, 'Name', True, False]
# print(number[4])   #   5
# print(number[-1])  #   False

""" 
number = ["Name", 85, True, False]
one, two, three, four = number
print(two)     #   85 
"""

"""                                                             #  Name
number = ["Name", 85, True, False]                          #  85
for value in number:                                        #  True         
    print(value)                                            #  False  
"""

""" 
number = ["Name", 85, True, False]
i = 0
while i < len(number):
    print(number[i])
    i += 1
print(i)                 #  4 
"""

""" 
number = ["Name", 85, True, False]
names1 = ["Ururu", "Bob", "Yan"]
names2 = ["Regina", "Ilya", "Egor"]
if names1 == names2:
    print("Списки одинаковые")
else:
    print("Списки имеют разные значения")            #  Списки имеют разные значения 
"""

""" 
number = ["Name", 85, True, False]
names = ["Ururu", "Bob", "Yan", "Regina", "Ilya", "Egor", "Marta", "Artem"]
firstPart = names[:5]      
print(firstPart)           #  ['Ururu', 'Bob', 'Yan', 'Regina', 'Ilya']
"""

""" 
number = ["Name", 85, True, False]
names = ["Ururu", "Bob", "Yan", "Regina", "Ilya", "Egor", "Marta", "Artem"]
firstPart = names[start:end:step]
print(firstPart) 
"""    


#  append(item) - добавить в конец
#  insert(index, item) - добавляет элемент item  в список по индексу
#  extend(items) - добавляет набор элементов в конец списка
#  remove(item): удаляет элемент item. Удаляется только первое вхождение элемента. Если элемент не найден, генерирует исключение ValueError
#  clear(): удаление всех элементов из списка
#  index(item): возвращает индекс элемента item. Если элемент не найден, генерирует исключение ValueError
#  pop([index]): удаляет и возвращает элемент по индексу index. Если индекс не передан, то просто удаляет последний элемент.
#  count(item): возвращает количество вхождений элемента item в список
#  sort([key]): сортирует элементы. По умолчанию сортирует по возрастанию. Но с помощью параметра key мы можем передать функцию сортировки.
#  reverse(): расставляет все элементы в списке в обратном порядке
#  copy(): копирует список
#  Кроме того, Python предоставляет ряд встроенных функций для работы со списками:
#  len(list): возвращает длину списка
#  sorted(list, [key]): возвращает отсортированный список
#  min(list): возвращает наименьший элемент списка
#  max(list): возвращает наибольший элемент списка

""" 
names = ["Ururu", "Bob", "Yan", "Regina", "Ilya", "Egor"]
copynames = names.copy()
print(copynames)               #  ['Ururu', 'Bob', 'Yan', 'Regina', 'Ilya', 'Egor']
"""

""" 
numbers = [-10, -5, -4, -3, -2, -1, 0, 1, 2, 3]
def filt(numbers):
    return numbers > 1

result = filter(filt, numbers)                  #  (filt, numbers)(lambda n: n > 1, numbers) 

for n in result: print(n, end = " ")    # 2 3
 """

""" 
numbers = [-10, -5, -4, -3, -2, -1, 0, 1, 2, 3]
result = filter(lambda n: n < 2, numbers) 
for n in result: print(n, end = " *")        #   -10 *-5 *-4 *-3 *-2 *-1 *0 *1 *
 """


""" 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [Person("Regina", 20), Person("UruruGOD", 16), Person("Bob String", 99)]

view = filter(lambda p: p.age > 33, people)
for pers in view:
    print(f"Name: {pers.name}")                #   Name: Bob String 
"""


""" 
value = [1,2,3,4,5,6,7]
result = map(lambda n: n * n, value)
for n in result: print(n, end = " ")

people = [
    ["Regina", "10"],
    ["Ilya", 12],
    ["Yarik", 11],
]

print(people[2][0])      #  ?
 """


"""                                                                 Задача                                                                   """

# 1 Пусть дан список-матрица, который содержит три списка: Выведите всю матрицу в одном выражении.
#   Выведите всю матрицу в одном выражении.
#   Выведите по отдельности каждую строку матрицы.
#   Выведите по отдельности каждый элемент матрицы.

""" 
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

print(mat)
print(mat[0])
print(mat[1])
print(mat[2])
print(mat[0][0])
print(mat[0][1])
print(mat[0][2])
print(mat[1][0])
print(mat[1][1])
print(mat[1][2])
print(mat[2][0])
print(mat[2][1])
print(mat[2][2]) 
"""

# 2 Выведите элементы матрицы с помощью циклов, чтобы получился следующий консольный вывод:

""" 
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

# вывод матрицы с помощью цикла
for i in range(3):
    for j in range(3):
        print(mat[i][j], end = " ")
    print() # перевод на другую строку 
"""

""" 
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in mat:  # проход по строкам
    for elem in row:  # проход по элементам строки
        print(elem, end=" ")
    print()
 """

""" 
mat = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

for row in mat:
    print(' '.join(map(str, row)))
 """


list1 = [10, 20, 10, 20, 30, 40, 30, 50]
# список, который будет содержать уникальные элементы
list2 = []
# перебираем все элементы первого списка
for n in list1:
    if n not in list2:
        list2.append(n)
 
 
print ("Начальный список: ", list1)
print ("После удаления дублей: ", list2)



# списки чисел
numbers = []
squares = []
cubes = []
# начальное и конечное значения диапазона
start = 1
end = 11
# цикл добавления чисел в список
for count in range (start, end) :
    numbers.append (count)
    squares.append (count**2)
    cubes.append (count**3)
 
print ("numbers: ",numbers)        #  numbers:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print ("squares: ",squares)        #  squares:  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print ("cubes : ",cubes)           #  cubes :  [1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

""" 
# исходный список
list = [11, 22, 33, 44, 55]
print ("Начальный список: ", list)
 
# в цикле перебираем элементы и удаляем те, которые деляться на 2 без остатка
for i in list:
    if(i%2 == 0):
        list.remove(i)
         
print ("Список с нечетными числами: ", list)


# list_ = [11, 22, 33, 44, 55]
# list_ = [x for x in list_ if x % 2 != 0]  # используем list comprehension
# print(list_)
 """



