"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    mylist = []
    for number in numbers:
        mylist.append(number**2)
    return mylist


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def filter_numbers(list_number, *arg):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    mylist = []
    if arg[0] == 'odd':
        for i in list_number:
            if i%2 :
                mylist.append(i)
    elif arg[0] == 'even':
        for i in list_number:
            if not i%2 :
                mylist.append(i)
    elif arg[0] == 'prime':
        for i in list_number:
            d = 2
            while i%d != 0:
                d += 1
            if d == i :
                mylist.append(i)
    return mylist
