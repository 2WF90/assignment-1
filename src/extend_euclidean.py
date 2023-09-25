from src.integer import Integer
from src.basic_arithmetic import subtract
from src.division import *
from src.helpers import *
from src.multiplication import *

def extended_euclidean(x: Integer, y: Integer) -> tuple[Integer, Integer, Integer]:
    x_prime = x
    y_prime = y

    a_1 = Integer([1], False, x.radix)
    a_2 = Integer([0], False, x.radix)
    b_1 = Integer([0], False, y.radix)
    b_2 = Integer([1], False, y.radix)

    if x.to_string() == "0":
        return (a_2.to_string(), b_2.to_string(), y.to_string())
    elif y.to_string() == "0":
        return (a_1.to_string, b_1.to_string, x.to_string())

    while not y_prime.is_negative and not y_prime.exponents == [0]:
        q, r = divide(x_prime, y_prime)

        x_prime = y_prime
        y_prime = r

        a_3 = subtract(a_1, multiplication_primary(q, a_2))
        b_3 = subtract(b_1, multiplication_primary(q, b_2))

        a_1 = a_2
        b_1 = b_2

        a_2 = a_3
        b_2 = b_3

    d = x_prime

    a = a_1.to_string() if not (x_prime.is_negative and x_prime == Integer([0], False, x.radix)) else a_1.set_negative
    b = b_1.to_string() if not (y_prime.is_negative and y_prime == Integer([0], False, y.radix)) else b_1.set_negative

    return (a, b, d.to_string())

