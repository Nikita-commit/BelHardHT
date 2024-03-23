"""Написать док стринг к классу ShoppingCart.
Написать док стрингу к каждому методу этого класса."""


class ShoppingCart:
    """Класс ShoppingCart предназначен для создания/обновления списка покупок

    Класс ShoppingCart содержит в себе 3 атрибута: shopping_list, name, quantity:
        shopping_list - атрибут класса, является списком продуктов в виде dict();
        name - атрибут объекта, который отвечает за наименование продукта;
        quantity - атрибут объекта, отвечает за количество конкретного продукта.

    Метод add_list() создаёт список покупок.
    Метод update_list() обновляет список.

    """
    shopping_list = dict()
    name: str
    quantity: int

    def __init__(self, name, quantity):
        """Инициализирует атрибуты.

        :name - название продукта
        :type name: str

        :quantity - количество конкретного продукта
        :type quantity: int
        """
        self.name = name
        self.quantity = quantity

    def add_list(self):
        """Создает список покупок.

        :self.name - ключ(название продукта)
        :type self.name: str

        :self.quantity - значение(количество конкретного продукта)
        :type quantity: int
        """
        self.shopping_list[self.name] = self.quantity
        print(self.shopping_list)

    def update_list(self, new_name, new_quantity):
        """Обновляет список покупок. Проверяет, есть ли добавляемая покупка в списке: если
        есть - суммирует количество, если нет - создает новый ключ с названием покупки.

        :new_name - ключ(название продукта)
        :new_name: str

        :new_quantity - значение(количество конкретного продукта)
        :new_quantity: int
        """
        if new_name in self.shopping_list:
            self.shopping_list[new_name] += new_quantity
        else:
            self.shopping_list[new_name] = new_quantity
        print(self.shopping_list)


name_buy = input("Введите название продукта: ")
quantity_buy = int(input("Введите количество продукта: "))

shopping_list1 = ShoppingCart(name_buy, quantity_buy)
shopping_list1.add_list()

is_true = bool
while is_true:
    new_name_buy = input("\nВведите название нового продукта: ")
    new_quantity_buy = int(input("Введите количество продукта: "))
    shopping_list1.update_list(new_name_buy, new_quantity_buy)

