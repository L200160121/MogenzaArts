# NAMA              :    FIRZA AFFAN HARISTA
# NIM               :    L200160121


def ab(a, b):
    while a % b != 0:
        old_a = a
        old_b = b
        a = old_b
        b = old_a % old_b
    return b


class Fraction:
    def __init__(self, a, b):
        x = a / ab(a, b)
        y = b / ab(a, b)
        print(int(x), '/', int(y))

Fraction(1, 2)
Fraction(5, 10)
Fraction(-10, 20)
Fraction(4.0, 10.0)
