''' Задание 4 - С помощью декораторов реализовать конвейер сборки бургера
Написать декоратор bread, который:
- до декорируемой функции будет печатать
"</------------\\>"
- после декорируемой функции будет
печатать "<\\____________/>"
Написать декоратор tomato, который:
- до декорируемой функции будет печатать
"*** помидоры ****"
Написать декоратор salad, который:
- до декорируемой функции будет
печатать "~~~~ салат ~~~~~"
Написать декоратор cheese, который:
- до декорируемой функции будет
печатать "^^^^^ сыр ^^^^^^"
Написать декоратор onion, который:
- до декорируемой функции будет
печатать "----- лук ------"
Написать функцию beef, которая:
- печатает "### говядина ###"
Написать функцию chicken, которая:
- печатает "|||| курица ||||" '''


def bread_dec(func):
    def print_bread():
        return f"</------------\\> {func()} <\\____________/>"
    return print_bread


def tomato_dec(func):
    def print_tomato():
        return f"*** помидоры **** {func()}"
    return print_tomato


def salad_dec(func):
    def print_salad():
        return f"~~~~ салат ~~~~~ {func()}"
    return print_salad


def cheese_dec(func):
    def print_cheese():
        return f"^^^^^ сыр ^^^^^^ {func()}"
    return print_cheese


def onion_dec(func):
    def print_onion():
        return f"----- лук ------ {func()}"
    return print_onion


@bread_dec
@onion_dec
@tomato_dec
def beef_func():
    return "### говядина ###"


@bread_dec
@cheese_dec
@salad_dec
def chicken_func():
    return "|||| курица ||||"


print(beef_func())
print(chicken_func())

