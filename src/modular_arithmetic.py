from src.basic_arithmetic import add, subtract
from src.integer import Integer
from src.reduction import reduce


def mod_add(x: Integer, y: Integer, modulus: Integer) -> Integer:
    z_prime = add(x, y)

    if subtract(z_prime, modulus).is_negative:
        z = z_prime
    else:
        z = subtract(z_prime, modulus)

    return reduce(z, modulus)

def mod_subtract(x: Integer, y: Integer, modulus : Integer) -> Integer:
    z_prime = subtract(x, y)

    if not z_prime.is_negative:
        z = z_prime
    else:
        z = add(z_prime, modulus)

    return reduce(z, modulus)

