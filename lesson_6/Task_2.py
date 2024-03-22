''' Задание 2 - Написать функцию count_char, которая принимает строковое значение
STR_VAL,
из которого создает и возвращает словарь, следующего вида:
{
'буква': количество-вхождений-в-строку
}
например: {
'p': 2,
'y': 1,
}
STR_VAL = 'python is the fastest-growing major programming language'
Нельзя пользоваться collections.Counter! '''

STR_VAL = 'python is the fastest-growing major programming language'


def count_char(new_str: str):
    new_dict = {}
    for i in new_str:
        if i != ' ':
            if i in new_dict:
                new_dict[i] += 1
            else:
                new_dict[i] = 1
        else:
            continue

    return new_dict


print(count_char(STR_VAL))
