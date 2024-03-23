"""Создать класс Phone, у которого будут следующие атрибуты:
Определить атрибуты
    - brand - бренд
    - model - модель
    - issue_year - год выпуска
Определить методы:
    - инициализатор __init__
    - receive_call, который принимает имя звонящего и выводит на экран: Звонит {name}
    - get_info, который будет возвращать кортеж (brand, model, issue_year)
    - метод __str__, который выводит на экран информацию об устройстве:
        Бренд: {}
        Модель: {}
        Год выпуска: {}"""


class Phone:
    brand: str
    model: str
    issue_year: int
    new_dict: tuple

    def __init__(self, brand, model, issue_year):
        self.brand = brand
        self.model = model
        self.issue_year = issue_year

    def receive_call(self, name):
        print(f"Звонит '{name}'\n")

    def get_info(self):
        self.new_dict = (self.brand, self.model, self.issue_year)
        print(self.new_dict)

    def __str__(self):
        print(f"Бренд: {self.brand}\nМодель: {self.model}\nГод выпуска: {self.issue_year}\n")


name_caller = input("Введите имя звонящего: ")
phone_brand = input("Введите бренд смартфона: ")
phone_model = input("Введите модель: ")
phone_issue_year = input("Введите год выпуска: ")
phone_1 = Phone(phone_brand, phone_model, phone_issue_year)

while phone_1:
    print("\n1 - метод receive_call(), 2 - метод get_info(), 3 - метод __str__()")
    choice = int(input("Выберите желаемое действие(введите цифру от 1 до 3): "))
    if choice == 1:
        phone_1.receive_call(name_caller)
    elif choice == 2:
        phone_1.get_info()
    elif choice == 3:
        phone_1.__str__()
    else:
        print("Введите цифру от 1 до 3!\n")
