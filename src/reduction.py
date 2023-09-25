from src.basic_arithmetic import add, subtract
from src.division import divide
from src.integer import Integer
from src.multiplication import multiplication_karatsuba


def reduction(x: Integer, modulus: Integer) -> Integer:
    # check if the modulus is zero (no reduction needed)
    if modulus.strip_pad().exponents == [0]:
        return Integer([], False, x.radix)

    # perform the reduction by finding the remainder after division
    return divide(x, modulus)[1]


radices_divided_by_moduli = {}


def barrett_reduction(x: Integer, modulus: Integer) -> Integer:
    # check if the modulus is zero (no reduction needed)
    if modulus.strip_pad().exponents == [0]:
        return Integer([], False, x.radix)

    n = len(modulus)

    if (x.radix, modulus.to_string()) not in radices_divided_by_moduli:
        mu = divide(Integer([0] * (2 * n) + [1], False, x.radix), modulus)[0]
        radices_divided_by_moduli[(x.radix, modulus.to_string())] = mu

    q_0 = x.divide_by_radix(n - 1)
    q = multiplication_karatsuba(
        radices_divided_by_moduli[(x.radix, modulus.to_string())], q_0
    ).divide_by_radix(n + 1)

    r_1 = x.modulus_radix(n + 1)
    r_2 = multiplication_karatsuba(q, modulus).modulus_radix(n + 1)

    if subtract(r_2, r_1).is_negative:
        y = subtract(r_1, r_2)
    else:
        y = add(subtract(r_1, r_2), Integer([0] * (n + 1) + [1], False, x.radix))

    while subtract(modulus, y).is_negative:
        y = subtract(y, modulus)

    return y
