''' Задание 1 - Напишите функцию yes_or_no, которая принимает список из целых чисел,
проходит по нему и выводит Yes, если число уже встречалось и No, если нет '''


def yes_or_no(data: list):
    for ind, elem in enumerate(data):
        if elem in data[:ind]:
            print('Yes')
        else:
            print('No')


my_list = [1, 2, 3, 4, 5, 10, 1, 2]

print(yes_or_no(my_list))

