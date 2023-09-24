from division import divide, multiply
from src.basic_arithmetic import add, subtract


# Computes the modular inverse for a mod m. If it exists.
def ModInverse(a: int, modulus: int):
    xOne = 1
    xTwo = 0
    while modulus > 0:
        q, _ = divide(a, m)
        r = subtract(a, multiply(q, m))
        a = m
        m = r
        xThree = subtract(xOne, multiply(q, xTwo))
        xOne = xTwo
        xTwo = xThree
        pass

    if a == 1:
        inverse = xOne
        return inverse

    return None
