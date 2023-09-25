from src.division import divide
from src.integer import Integer
from src.basic_arithmetic import subtract
from src.multiplication import multiplication_karatsuba as multiply


# Computes the modular inverse for a mod m. If it exists.
def ModInverse(x: Integer, modulus: Integer) -> Integer:
    xOne = Integer.from_string('1', 10)
    xTwo = Integer.from_string('0', 10)

    while BiggerThanZero(modulus):
        q, r = divide(x, modulus)
        x = modulus
        modulus = r
        xThree = subtract(xOne, multiply(q, xTwo))
        xOne = xTwo
        xTwo = xThree

    if len(x) == 1 and x.exponents[0] == 1:
        inverse = xOne

        return inverse

    return Integer([], False, x.radix)

def BiggerThanZero(m: Integer) -> bool:
    if len(m) > 1:
        return True
    elif m.is_negative == False and m.exponents[0] != 0:
        return True
    return False
