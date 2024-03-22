'''Задание 3 - Написать функцию hello, которая принимает аргумент name - строку с именем и
выводит принтом "Привет, {name}"
Написать декоратор log_decorator, который перед выполнением
функции печатает на экран строку, вида
"Выполняем {func.__name__} с args: {args} и kwargs: {kwargs}".
После выполнения функции напечатать строку "Выполнено {func.__name__} '''


def log_decorator(func):
    def print_func(*args, **kwargs):
        print(f'Выполняем {func} с args: {args} и kwargs: {kwargs}')
        hello_func = func(*args, **kwargs)
        print(f'Выполнено {func}')
        return hello_func
    return print_func


new_name = input("Введите ваше имя: ")


@log_decorator
def hello(name: str):
    print(f'Привет, {name}')


hello(new_name)
