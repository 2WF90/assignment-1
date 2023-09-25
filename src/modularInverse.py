from src.division import divide
from src.integer import Integer
from src.basic_arithmetic import subtract, add
from src.multiplication import multiplication_karatsuba as multiply


# Computes the modular inverse for a mod m. If it exists.
def ModInverse(x: Integer, modulus: Integer) -> Integer:
    newModulus = modulus

    #1.2
    xOne = Integer.from_string('1', 10)
    xTwo = Integer.from_string('0', 10)

    _, x = divide(x, newModulus)

    #2.1
    while BiggerThanZero(newModulus):
        #2.2
        q, r = divide(x, newModulus)
        #2.3
        x = newModulus
        newModulus = r
        #2.4
        xThree = subtract(xOne, multiply(q, xTwo))
        #2.5
        xOne = xTwo
        xTwo = xThree

    if len(x) == 1 and x.exponents[0] == 1:
        inverse = xOne
        # while inverse.is_negative == True:
        #     inverse = add(inverse, modulus)

        # _, inverse = divide(xOne, modulus)

        return inverse

    return Integer([], False, x.radix)

def BiggerThanZero(m: Integer) -> bool:
    if len(m) > 1:
        return True
    elif m.is_negative == False and m.exponents[0] != 0:
        return True
    return False
