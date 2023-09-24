from src.division import divide
from src.integer import Integer


def reduce(x: Integer, modulus: Integer) -> Integer:
    if (modulus.strip_pad().exponents == [0]):
        return Integer([], False, x.radix)

    return divide(x, modulus)[1]
