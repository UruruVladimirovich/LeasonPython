""" 
Задание 1: Классы и объекты
Создайте класс Student с следующими атрибутами:
name (имя студента)
age (возраст студента)
grades (список оценок)
Добавьте методы:
add_grade(grade) - добавляет оценку в список оценок
get_average() - возвращает средний балл студента 
"""

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades
    
    def get_info(self):
        print(f'Оценки студента {self.name} возрастом {self.age}: {self.grades}')
        print(f'Средняя оценка: {sum(self.grades) / len(self.grades)}')

newStudent = Student('Вуглускр', 20, [4, 5, 3])
newStudent.get_info()


    # def get_average(self):
    #     return sum(self.grades) / len(self.grades)
    #print(newStudent.get_average())