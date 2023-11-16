import click
from pizza import Margherita, Pepperoni, Hawaiian, bake, delivery, pickup


@click.group()
def cli():
    pass


@cli.command()
@click.option('--d', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
@click.argument('size', nargs=1)
def order(pizza: str, size: str, d: bool):
    """
    Готовит и доставляет пиццу
    Ключи:
      --d   -   доставка
    """
    pizza = pizza.lower()

    pizzas = {
        'margherita': Margherita,
        'pepperoni': Pepperoni,
        'hawaiian': Hawaiian
    }

    if pizza not in pizzas:
        raise ValueError('Unavailable type of pizza.'
                         'You can check menu by call \'cli.py menu\'')

    pizza = pizzas[pizza](size)
    bake(pizza)

    if d:
        delivery(pizza)
    else:
        pickup(pizza)


@cli.command()
def menu():
    """
    Выводит меню
    """
    pizzas = [Margherita('L'), Pepperoni('L'), Hawaiian('L')]
    for pizza in pizzas:
        print(f'- {pizza.name}: {", ".join(pizza.ingredients)}')


if __name__ == '__main__':
    cli()
