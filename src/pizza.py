import random
from decorators import log


class Pizza:
    """
    Класс Pizza, обозначающий основу пиццы
    size - размер пиццы, L или XL.
    """
    def __init__(self, size: str):
        if size not in ('L', 'XL'):
            raise ValueError('Incorrect size of pizza. Available sizes: L, XL')
        self.name = 'Base pizza'
        self.ingredients = ['tomato sauce', 'mozzarella']
        self.size = size

    def __dict__(self):
        return {self.name: self.ingredients}

    def __eq__(self, other):
        """
        Проверяет 2 пиццы на эквивалентность.
        """
        if not isinstance(other, Pizza):
            raise TypeError('incorrect type for comparison')
        return sorted(self.ingredients) == sorted(other.ingredients) and \
            self.name == other.name and self.size == other.size


class Margherita(Pizza):
    """
    Класс Margherita, обозначающий пиццу Маргарита
    """
    def __init__(self, size: str):
        super().__init__(size)
        self.name = 'Margherita 🧀'
        self.ingredients.extend(['tomatoes'])


class Pepperoni(Pizza):
    """
    Класс Pepperoni, обозначающий пиццу Пепперони
    """
    def __init__(self, size: str):
        super().__init__(size)
        self.name = 'Pepperoni 🍕'
        self.ingredients.extend(['pepperoni'])


class Hawaiian(Pizza):
    """
    Класс Hawaiian, обозначающий гавайскую пиццу с ананасами
    """
    def __init__(self, size: str):
        super().__init__(size)
        self.name = 'Hawaiian 🍍'
        self.ingredients.extend(['chicken', 'pineapple'])


@log('Приготовили за {} с.')
def bake(pizza: Pizza):
    """
    Готовит пиццу
    """
    print(f'Готовим {pizza.name}, {pizza.size}. '
          f'Примерное время ожидания: {random.randint(2, 5)} с.')


@log('Доставили за {} с.')
def delivery(pizza: Pizza):
    """
    Доставляет пиццу
    """
    print(f'Пицца {pizza.name} готова. '
          f'Примерное время доставки: {random.randint(2, 5)} с.')


@log('Забрали за {} с.')
def pickup(pizza: Pizza):
    """
    Самовывоз пиццы
    """
    print(f'Пицца {pizza.name} готова. Ожидаем самовывоз.')
