firstname = 'Никита'
lastname = 'Кухарский'
age = 23

print(f"Привет, меня зовут {firstname} {lastname}, мне {age} года")
# -----------------------

first_word = input("Введите слово: ")
second_word = first_word[2]

print(second_word)
# -----------------------

first_word = input("Введите слово: ")
second_word = first_word[-2]

print(second_word)
# -----------------------

first_word = input("Введите слово: ")
second_word = first_word[0:5]

print(second_word)
# -----------------------

first_word = input("Введите слово: ")
second_word = first_word[:-2]

print(second_word)
# -----------------------

name = input("Введите имя: ")
some_str = "Hello, world!"

print(some_str.replace("world", name))


