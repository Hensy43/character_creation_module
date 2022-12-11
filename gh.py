from math import sqrt

massage: str = (
    'Добро пожаловать в самую лучшую программу для вычисления '
    'квадратного корня из заданного числа')
print(f'{massage}')


def calculate_square_root(number):
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number):
    """Выводит результат на терминал."""
    if your_number < 0:
        return print('Корень из отрицательного числа извлечь нельзя!')
    result = calculate_square_root(your_number)
    if your_number >= 0:
        return print(
            f'Мы вычислили квадратный корень из'
            f' введённого вами числа. Это будет: {result}',
        )
    return print(
        'Не удалось вычислить квадратный корень из введённого вами числа')


calc(1)
