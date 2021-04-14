# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

print('Тип данных "NoneType"')
None_Type = None
if None_Type == None:
    print("Error 403")

print('Тип данных "Числа"')
numbers = int('10001', 2)
print(numbers)

print('Тип данных "Строки"')
first_str = "Hello"
last_str = "World"
str = f"{first_str} {last_str}"
print(str)

print('Тип данных "Списки"')
list = [2, 6, 5, 36, 20, 47, 55, 4, 7, 22, 1]
print(list)

list.remove(55)
print(list)

list.append(10)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

print('Тип данных "Кортеж"')
Tuple = (1, 2, 3)
print(Tuple)
print(Tuple.count(2))
print(Tuple.index(3))

print('Тип данных "Множества"')
set_a = [1, 2, 3, 0, 1, 2, 3]
print(set(set_a))
set_b = set(set_a)
set_b.add(4)
print(set_b)

print('Тип данных "Замороженные множества"')
fset = frozenset(set_b)
print(fset)

print('Тип данных "Байты" и "Массив байт')
byte_str = b"Hello"
byte_array_str = bytearray(byte_str)
print(byte_str)

print('Тип данных "Булевый"')
bool_a = bool(1)
print(bool_a)

print('Тип данных "Словари"')
dict = {"name": "Yuriy", "surname": "Vorobey"}
print(dict["name"])
print(dict.get("surname"))
print(dict.get("age"))
if dict.get("age")== None:
    print("Возраст не задан")
    dict = {"name": "Yuriy", "surname": "Vorobey", "age": input("Введите ваш возраст ")}
print(dict.get("name"))
print(dict.get("surname"))
print(dict.get("age"))

type_list = [None_Type, numbers, str, list, Tuple, set_a, fset, byte_str, byte_array_str, bool_a, dict]
for i in type_list:
    print(f'{i} "Тип данных: " {type(i)}')