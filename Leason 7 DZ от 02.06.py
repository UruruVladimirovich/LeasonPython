
# my_tuple = (1, 2, 3, 4, 5, 6)
# print(my_tuple[4:])         #  (5, 6)
# print(my_tuple[4])          #  5


# my_tuple1 = (1, 2, 3, 4, 5, 6)
# myElement = my_tuple1[5]

""" 
for i in range(200, 300, 50):
    print(i)     #  200     250
"""
""" 
number = list(range(200))
print(number)     #   [0, 1, ....198, 199]
 """

#  Словарь (dictionary)

# emptyDict = dict()
""" 
user = {
    1: "Значение",
    "Ключ": True
}
print(user)        #  {1: 'Значение', 'Ключ': True}
 """

""" 
user_list = [
    ["Key", "Value"]
]

newDict = dict(user_list)
print(type(newDict))            #  <class 'dict'>
 """


# # dictionary[key]

# user_list = [
#     ["Key", "Value"]
# ]

# newDict = dict(user_list)
# print(newDict)             #  {'Key': 'Value'}
# print(newDict["Key"])         #  Value
# newDict["Key"] = "Свой ключ"
# print(newDict)      #  {'Key': 'Свой ключ'}


# myValue = newDict.get("Key1")
# print(myValue)     #  None

# #  Если метод get не нашел значение он возращает None

# del newDict["Key"]
# print(newDict)      #  {}

""" 
#  на основе списка, сделайте словарь. Поменяйте значение по ключу, переберите словарь и выведите результат в консоль
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c', 'd', 'e', 'f']
my_dict11 = dict(zip(list1, list2))
print(my_dict11)
 """                                    #  ????



# Комплексные словари

""" 
users = {
    "user1": {
        'name': 'Ururu',
        'phone': 666
    },
    "user2": {
        'name': 'Bob',
        'phone': 666999
    }
}

admin = users['user1']['name']
print(admin)                   #  Ururu
admin = users['user2']['phone']
print(admin)                   #  666999
admin = users['user1']['name'] = "Robert"
print(admin)                  #  Robert
 """

""" 
users = {
    "user1": {
        'name': 'Ururu',
        'phone': 666
    },
    "user2": {
        'name': 'Bob',
        'phone': 666999
    }
}

admin = users['user2'].get('Lee', "Ничего, Тут нет Lee")
print(admin)                #  Ничего, Тут нет Lee
 """


number = list(range(0,300,10))
num = number[10:20]
print(num)
tuple1 = tuple(num)
print(tuple1)
tuple2 = list(tuple1)
print(tuple2)
ILoveAcademy=[]                         #  ILoveAcademy = [i for i in tuple2]
for i in tuple2:
    ILoveAcademy.append(i)

print(f"Футуре тупле", ILoveAcademy)