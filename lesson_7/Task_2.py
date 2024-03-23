"""Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя."""


class Dog:
    height: int
    weight: int
    name: str
    age: int

    def __init__(self, height, weight, name, age):
        self.height = height
        self.weight = weight
        self.name = name
        self.age = age

    def jump(self):
        print("Собака прыгает")
        print(f"Рост собаки - {self.height}, вес собаки - {self.weight}, кличка - '{self.name}', возраст - {self.age}")

    def run(self):
        print("Собака бегает")
        print(f"Рост собаки - {self.height}, вес собаки - {self.weight}, кличка - '{self.name}', возраст - {self.age}")

    def bark(self):
        print("Собака лает")
        print(f"Рост собаки - {self.height}, вес собаки - {self.weight}, кличка - '{self.name}', возраст - {self.age}")

    def change_name(self, name):
        self.name = name
        print(f"Рост собаки - {self.height}, вес собаки - {self.weight}, кличка - '{self.name}', возраст - {self.age}")


dog_1 = Dog(5, 20, 'Чарли', 8)

while dog_1:
    print("\n1 - метод jump(), 2 - метод run(), 3 - метод bark()")
    choice = int(input("Выберите желаемое действие(введите цифру от 1 до 4): "))
    if choice == 1:
        dog_1.jump()
    elif choice == 2:
        dog_1.run()
    elif choice == 3:
        dog_1.bark()
    elif choice == 4:
        new_name = input("Введите новую кличку: ")
        dog_1.change_name(new_name)
    else:
        print("Введите цифру от 1 до 4!\n")
