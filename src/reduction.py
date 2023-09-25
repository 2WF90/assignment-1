from src.division import divide
from src.integer import Integer


def reduction(x: Integer, modulus: Integer) -> Integer:
    # check if the modulus is zero (no reduction needed)
    if modulus.strip_pad().exponents == [0]:
        return Integer([], False, x.radix)

    # perform the reduction by finding the remainder after division
    return divide(x, modulus)[1]
