import pytest
from click.testing import CliRunner
from src.cli import menu, order
from src.pizza import Pizza, Margherita, Pepperoni, Hawaiian
import re


def test_menu():
    runner = CliRunner()
    res = runner.invoke(menu)
    expected = '- Margherita 🧀: tomato sauce, mozzarella, tomatoes\n' \
               '- Pepperoni 🍕: tomato sauce, mozzarella, pepperoni\n' \
               '- Hawaiian 🍍: tomato sauce, mozzarella, chicken, pineapple\n'
    assert res.output == expected


@pytest.mark.parametrize(
    'pizza_name, pizza, size',
    [
        ('margherita', Margherita('L'), 'L'),
        ('PePpErOnI', Pepperoni('XL'), 'XL'),
        ('Hawaiian', Hawaiian('XL'), 'XL')
    ]
)
def test_order_delivery(pizza_name: str, pizza: Pizza, size: str):
    runner = CliRunner()
    res = runner.invoke(order, [pizza_name, size, '--d'])
    assert re.fullmatch(f'Готовим {pizza.name}, {size}\\. '
                        f'Примерное время ожидания: [2-5] с\\.\n'
                        f'Приготовили за [2-5] с\\.\n'
                        f'Пицца {pizza.name} готова\\. '
                        f'Примерное время доставки: [2-5] с\\.\n'
                        f'Доставили за [2-5] с\\.\n', res.output)


@pytest.mark.parametrize(
    'pizza_name, pizza, size',
    [
        ('margherita', Margherita('L'), 'L'),
        ('PePpErOnI', Pepperoni('XL'), 'XL'),
        ('Hawaiian', Hawaiian('XL'), 'XL')
    ]
)
def test_order_pickup(pizza_name: str, pizza: Pizza, size: str):
    runner = CliRunner()
    res = runner.invoke(order, [pizza_name, size])
    assert re.fullmatch(f'Готовим {pizza.name}, {size}\\. '
                        f'Примерное время ожидания: [2-5] с\\.\n'
                        f'Приготовили за [2-5] с\\.\n'
                        f'Пицца {pizza.name} готова\\. '
                        f'Ожидаем самовывоз\\.\n'
                        f'Забрали за [2-5] с\\.\n', res.output)


def test_order_except():
    runner = CliRunner()
    res = runner.invoke(order, ['Ajkhfasjhsf', 'XL'])
    assert isinstance(res.exception, ValueError)
