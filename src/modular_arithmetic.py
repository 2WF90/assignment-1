from src.basic_arithmetic import add, subtract
from src.integer import Integer
from src.reduction import reduce


def mod_add(x: Integer, y: Integer, modulus: Integer) -> Integer:
    # calculate the sum without considering the modulus
    z_prime = add(x, y)

    # check if the result is negative with respect to the modulus
    if subtract(z_prime, modulus).is_negative:
        z = z_prime
    else:
        # if it's not negative, subtract the modulus to ensure it's within bounds
        z = subtract(z_prime, modulus)

    # reduce the result to ensure it's within the modulus range
    return reduce(z, modulus)


def mod_subtract(x: Integer, y: Integer, modulus: Integer) -> Integer:
    # calculate the difference without considering the modulus
    z_prime = subtract(x, y)

    # check if the result is not negative
    if not z_prime.is_negative:
        z = z_prime
    else:
        # if it's negative, add the modulus to wrap around within bounds
        z = add(z_prime, modulus)

    # reduce the result to ensure it's within the modulus range
    return reduce(z, modulus)
