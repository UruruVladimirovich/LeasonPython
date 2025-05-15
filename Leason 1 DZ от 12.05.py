# 1. Создайте переменную типа целое число и выведите её на экран.
satana = 666
print(satana)

# 2. Создайте переменную типа строка и выведите её длину.
name = 'Ururu'
print(name)  
print("Длина строки:", len(name))  

# 3. Создайте переменную булевого типа и выведите её значение.
II = 888
who_is_stronger = II > satana
print(who_is_stronger)

# 4. Напишите программу, которая запрашивает у пользователя число и выводит его квадрат.
number = float(input('Введите число 1: '))
square = number ** 2
print(f"Квадрат числа {number} равен {square}")

# 5. Напишите цикл for, который выводит числа от 1 до 10.
for n in range(0, 11, 1):
    print(n)

# 6. Напишите цикл while, который выводит числа от 10 до 1.
number1 = 10
while number1 >= 1:
    print(number1)
    number1 -= 1
print('Работа программы завершена') 

# 7. Создайте условие, которое проверяет, является ли введённое число положительным, отрицательным или нулём.
number2 = float(input("Введите число: "))
if number2 > 0:
    print("Число положительное")
elif number2 < 0:
    print("Число отрицательное")
else:
    print("Число равно нулю")

# 8. Напишите функцию, которая принимает два числа и возвращает их сумму.
def sum_numbers(a, b):
    return a + b

# 9. Создайте функцию, которая принимает строку и возвращает её в верхнем регистре.
def to_uppercase(input_string):
    return input_string.upper()

result = to_uppercase("Hello, World!")
print(result)

user_input = input("Введите строку: ")
print("Результат:", to_uppercase(user_input))

# 10.Напишите программу с использованием условных операторов и циклов для определения чётности чисел в списке.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Определение чётности чисел в списке:")
for number in numbers:
    if number % 2 == 0:
        print(f"{number} - чётное")
    else:
        print(f"{number} - нечётное")