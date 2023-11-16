from src.pizza import (
    Pizza,
    Margherita,
    Pepperoni,
    Hawaiian,
    bake,
    delivery,
    pickup
)
import pytest


def test_base_pizza_name():
    pizza = Pizza('L')
    assert pizza.name == 'Base pizza'


def test_base_pizza_ingredients():
    pizza = Pizza('XL')
    assert sorted(pizza.ingredients) == sorted(['tomato sauce', 'mozzarella'])


def test_pizza_incorrect_size():
    with pytest.raises(ValueError):
        Pizza('M')


def test_pizza_dict():
    pizza = Pizza('XL')
    assert pizza.__dict__() == {'Base pizza': ['tomato sauce', 'mozzarella']}


def test_margherita_name():
    pizza = Margherita('L')
    assert pizza.name == 'Margherita 🧀'


def test_pepperoni_name():
    pizza = Pepperoni('L')
    assert pizza.name == 'Pepperoni 🍕'


def test_hawaiian_name():
    pizza = Hawaiian('L')
    assert pizza.name == 'Hawaiian 🍍'


def test_margherita_recipe():
    pizza = Margherita('L')
    assert sorted(pizza.ingredients) == sorted(['tomato sauce',
                                                'mozzarella',
                                                'tomatoes'])


def test_pepperoni_recipe():
    pizza = Pepperoni('L')
    assert sorted(pizza.ingredients) == sorted(['tomato sauce',
                                                'mozzarella',
                                                'pepperoni'])


def test_hawaiian_recipe():
    pizza = Hawaiian('L')
    assert sorted(pizza.ingredients) == sorted(['tomato sauce',
                                                'mozzarella',
                                                'chicken',
                                                'pineapple'])


@pytest.mark.parametrize(
    'pizza',
    [
        (Margherita('L')),
        (Pepperoni('L')),
        (Hawaiian('L'))
    ]
)
def test_bake(pizza: Pizza, capsys):
    bake.__wrapped__(pizza)
    captured = capsys.readouterr().out
    expected = []
    for i in range(2, 6):
        expected.append(f'Готовим {pizza.name}, {pizza.size}. '
                        f'Примерное время ожидания: {i} с.\n')
    assert captured in expected


@pytest.mark.parametrize(
    'pizza',
    [
        (Margherita('L')),
        (Pepperoni('L')),
        (Hawaiian('L'))
    ]
)
def test_delivery(pizza, capsys):
    delivery.__wrapped__(pizza)
    captured = capsys.readouterr().out
    expected = []
    for i in range(2, 6):
        expected.append(f'Пицца {pizza.name} готова. '
                        f'Примерное время доставки: {i} с.\n')
    assert captured in expected


@pytest.mark.parametrize(
    'pizza',
    [
        (Margherita('L')),
        (Pepperoni('L')),
        (Hawaiian('L'))
    ]
)
def test_pickup(pizza, capsys):
    pickup.__wrapped__(pizza)
    captured = capsys.readouterr().out
    expected = f'Пицца {pizza.name} готова. Ожидаем самовывоз.\n'
    assert captured == expected
