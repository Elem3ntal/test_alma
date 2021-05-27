"""
los comentarios han sido omitidos en honor al tiempo
(en el futuro lo podemos conversar)

:Author:
    - Javier Rodríguez.

:Created:
    - 2021.05.27.
"""

def d(n):
    """
    """
    n_str = f'{n}'
    base = sum(int(_) for _ in n_str)
    return n + base


def main(args):
    """
    """
    target = 100
    try:
        target = int(args[1])
    except Exception:
        print('missing target number')

    list_number = set(_ for _ in range(1, target))
    numbers_generated = {*map(d, list_number)}
    numbers = sorted(list_number.difference(numbers_generated))
    print(numbers)
    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv))
