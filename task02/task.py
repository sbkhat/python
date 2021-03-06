# 1. Создать список и заполнить его элементами различных типов данных.
# Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

result_list = [2, 'text', '456', 45.3, None]
for el in result_list:
    print(type(el))

# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

result_list = []
i = 0
element = 0
while i < 3:
    result_list.append(input("Введите значение списка:"))
    i += 1

for el in range(int(len(result_list)/2)):
        result_list[element], result_list[element + 1] = result_list [element + 1], result_list[element]
        element += 2
print(result_list)

# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и через dict.
seasons_list = ['зима', 'весна', 'лето', 'осень']
seasons_dict = {1 : 'зима', 2 : 'весна', 3 : 'лето', 4 : 'осень'}
seasons_dict_ext = {
    1 : 'зима',
    2 : 'зима',
    3 : 'весна',
    4 : 'весна',
    5 : 'весна',
    6 : 'лето',
    7 : 'лето',
    8 : 'лето',
    9 : 'осень',
    10 : 'осень',
    11 : 'осень',
    12 : 'зима',
}
i = 0
month_number = int(input("Введите месяц по номеру "))
if month_number == 12 or month_number <= 2:
    i = 0
elif month_number >= 3 and month_number <= 5:
    i = 1
elif month_number >= 6 and month_number <= 8:
    i = 2
else:
    i = 3

print(seasons_list[i])
print(seasons_dict.get(i + 1))
print(seasons_dict_ext.get(month_number))



seasons_dict = {0 : 'зима', 1 : 'весна', 2 : 'лето', 3 : 'осень', 4: 'Такого месяца не существует'}
seasons_list = ['зима', 'весна', 'лето', 'осень', 'Такого месяца не существует']
month = int(input("Введите номер месяца  "))
month_index = 4
if month <= 2 or month == 12:
    month_index = 0
elif month >= 3 and month <= 5:
    month_index = 1
elif month == 6 or month == 7 or month == 8:
    month_index = 2
elif month == 9 or month == 10 or month == 11:
    month_index = 3
print(seasons_list[month_index])
print(seasons_dict.get(month_index))

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки.
# Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.
my_string = input("введите предложение ")
my_word = []
number = 1
for element in range(my_string.count(' ') + 1):
    my_word = my_string.split()
    if len(str(my_word)) <= 10:
        print(f" {number} {my_word [element]}")
        number += 1
    else:
        print(f" {number} {my_word [element] [0:10]}")
        number += 1

# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
print(f"Рейтинг - {my_list}")
digit = int(input("Введите число (-1 - выход) "))
while digit != -1:
    for el in range(len(my_list)):
        if my_list[el] == digit:
            my_list.insert(el + 1, digit)
            break
        elif my_list[0] < digit:
            my_list.insert(0, digit)
        elif my_list[-1] > digit:
            my_list.append(digit)
        elif my_list[el] > digit and my_list[el + 1] < digit:
            my_list.insert(el + 1, digit)
    print(f"текущий список - {my_list}")
    digit = int(input("Введите число (-1 - выход) "))

# 6. *Реализовать структуру данных «Товары».
# Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь
# с параметрами (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.
# Пример готовой структуры:
#
# [
#     (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
#     (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
#     (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
#
# Необходимо собрать аналитику о товарах.
# Реализовать словарь, в котором каждый ключ — характеристика товара, например название, а значение — список значений-характеристик, например список названий товаров.
#
# Пример:
#
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

inventory_tuple_list = []
i = 1
while True:
    inventory_tuple_list.append(
        (i, dict({
            'название': str(input('Введите название: ')),
            'цена': float(input('Введите цену: ')),
            'количество': int(input('Введите количество: ')),
            'eд': str(input('Введите единцы измерения: ')),
        }))
    )
    if input('Товар добавлен. Добавить еще один товар? (да/нет): ') == 'нет':
        break
    i += 1

output_dict = dict({})
for product in inventory_tuple_list:
    for key, value in product[-1].items():
        if key in output_dict:
            if value not in output_dict.get(key):
                output_dict.get(key).append(value)
        else:
            output_dict.update({key: [value]})


print(f'собрана аналитика: {output_dict}')