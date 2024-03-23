"""Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на
экран. Создать объект класса Dog, вызвать все методы объекта и вывести на
экран все его атрибуты."""


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


dog_1 = Dog(5, 20, 'Чарли', 8)

while dog_1:
    print("\n1 - метод jump(), 2 - метод run(), 3 - метод bark()")
    choice = int(input("Выберите желаемое действие(введите цифру от 1 до 3): "))
    if choice == 1:
        dog_1.jump()
    elif choice == 2:
        dog_1.run()
    elif choice == 3:
        dog_1.bark()
    else:
        print("Введите цифру от 1 до 3!\n")

