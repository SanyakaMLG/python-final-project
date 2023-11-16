import functools
import random
import time


def log(template: str = None):
    """
    Декоратор, подставляющий случайное число
    в строку-шаблон. По умолчанию - 'func_name - {} с.'
    :param template: Шаблон строки
    """
    def inner_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            sleep_time = random.randint(2, 5)
            time.sleep(sleep_time)
            if template is None:
                print(f'{func.__name__} - {sleep_time} с.')
            else:
                print(template.format(sleep_time))
            return res
        return wrapper
    return inner_decorator
