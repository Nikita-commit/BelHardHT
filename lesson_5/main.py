'''Задание 1 - В семье свадьба. Они решили выбрать заведение, где будут праздновать в
зависимости от количества людей, которое прибудет к утру. Если их будет больше 50 - закажут ресторан,
если от 20 до 50 -то кафе, а если меньше 20 - то отпраздную дома.
Вывести "ресторан", "кафе", "дом" в зависимости от количества гостей.'''

count_guests = ''

while len(str(count_guests)) < 1:
    try:
        print("Задание 1")
        count_guests = int(input("Введите количество гостей: "))

        if count_guests > 50:
            empty_variable = False
            print("Ресторан!")
        elif 20 <= count_guests <= 50:
            empty_variable = False
            print("Кафе!")
        elif 1 <= count_guests < 20:
            empty_variable = False
            print("Дом!")
        elif count_guests < 1:
            print("Неверное количество гостей!\n")
    except ValueError as val:
        print("Строка должна содержать какое-то значение!\n")


'''Задание 2 - Ввести строку. Если длина строки больше 10 символов, то создать новую строку с 3
восклицательными знаками в конце ('!!!') и вывести на экран. Если меньше 10, то
вывести на экран второй символ строки.'''

my_string = ''

while len(my_string) < 2:

    my_string = input("\nЗадание 2\nВведите строку: ")
    try:
        print(my_string + '!!!') if len(my_string) > 10 else print(my_string[1])

    except IndexError as ind:
        print("Строка должна содержать больше 2-х символов!")

'''Задание 3 - Получить на ввод количество рублей и копеек и вывести в правильной форме,
например, 3 рубля, 1 рубль 25 копеек, 3 копейки.
До 10р *
До 100р **
До 1000р ***'''

word_bool = True

while word_bool:

    count_ruble = input("\nЗадание 3\nВведите количество рублей: ")
    count_kopecks = input("Введите количество копеек: ")

    ending_ruble = ''
    ending_kopecks = ''
    list_of_numbers1 = [0, 5, 6, 7, 8, 9]
    list_of_numbers2 = [2, 3, 4]

    try:
        if len(count_ruble) == 0 and len(count_kopecks) == 0:
            print('Заполните хотя бы одно из предложенных полей!')

        elif len(count_ruble) != 0:
            if int(count_ruble[-1]) == 1:
                ending_ruble = 'рубль'
            elif int(count_ruble[-1]) in list_of_numbers1 or int(count_ruble[0]) == 1:
                ending_ruble = 'рублей'
            elif int(count_ruble[-1]) in list_of_numbers2:
                ending_ruble = 'рубля'

        if len(count_kopecks) != 0:
            if int(count_kopecks[-1]) == 1:
                ending_kopecks = 'копейка'
            elif int(count_kopecks[-1]) in list_of_numbers1:
                ending_kopecks = 'копеек'
            elif int(count_kopecks[-1]) in list_of_numbers2:
                ending_kopecks = 'копейки'
            if 0 < int(count_kopecks) <= 99:
                if len(count_ruble) != 0:
                    print(f"{count_ruble} {ending_ruble} {count_kopecks} {ending_kopecks}")
                else:
                    print(f"{count_kopecks} {ending_kopecks}")
            elif int(count_kopecks) == 0 or int(count_kopecks) > 99:
                print('Диапазон значений копеек должен быть от 1 до 99!')
        else:
            print(f"{count_ruble} {ending_ruble}")

    except ValueError as val:
        print("Введённые значения должны быть числового формата!")
