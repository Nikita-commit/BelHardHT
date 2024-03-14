# Задание 1.1 - Создать два списка произвольного содержания
new_list1 = [i for i in range(1, 11)]
new_list2 = ['Nikita', 'Roma', 'Sasha']

print(f'Задание 1.1\n{new_list1}\n{new_list2}')


# Задание 1.2 - Добавить к каждому списку по одному элементу в конец и в начало
new_list1.append('Python')
new_list1.insert(0, 'My')

new_list2.append(20)
new_list2.insert(0, 10)

print(f'\nЗадание 1.2\n{new_list1}\n{new_list2}')


# Задание 1.3 - Расширить первый список вторым
new_list1.extend(new_list2)

print(f'\nЗадание 1.3\n{new_list1}\n{new_list2}')


# Задание 2 - Создать два списка, с одинаковым кол-вом элементов. Сделать из этих списков словарь
print("Zen of Python")
key_list = [i for i in range(1, 6)]
value_list = ['Belarus', 'Minsk', 'Kukharskiy', 'Nikita', 'Igorevich']
new_dict = dict(zip(key_list, value_list))

print(f'\nЗадание 2\n{new_dict}\n')


# Задание 3.1 Определите количество строк в Дзене Питона.
print('Zen of Python'.center(225, '-'))
import this
zen_python = "".join([this.d.get(c, c) for c in this.s])
lines = len(zen_python.splitlines())

print(f'\nЗадание 3.1\nКоличество строк в zen of Python: {lines}')

# Задание 3.2 Подсчитайте количество вхождений ключевых слов из Дзена Питона, таких как "is", "and", "or". Сложить в
# словарь такого типа {“is”: 4, “and”: None, “or”: 100}
count_is = zen_python.count('is')
count_and = zen_python.count('and')
count_or = zen_python.count('or')

zen_dict = {}

zen_dict['is'] = count_is
zen_dict['and'] = count_and
zen_dict['or'] = count_or

print(f'\nЗадание 3.2\n{zen_dict}')


# Задание 3.3 Замените все вхождения слова "is" в Дзене Питона на "is not".
print(f'\nЗадание 3.3\n', zen_python.replace("is", "is not"))


