from src.integer import Integer
from src.basic_arithmetic import add, subtract


def divide(x: Integer, y: Integer) -> Integer:
    result_is_negative = x.is_negative ^ y.is_negative

    x = x.make_absolute()
    y = y.make_absolute()

    if y.exponents == [0]:
        raise ZeroDivisionError()

    r = x
    k = len(x) - len(y) + 1
    q = [0] * k

    for i in range(k - 1, -1, -1):
        b_i_y = Integer([0] * i + y.exponents, y.is_negative, y.radix)
        q[i] = get_quotient(r, b_i_y)

        r = subtract(r, multiply(Integer([q[i]], False, y.radix), b_i_y))

    q = Integer(q, result_is_negative, x.radix).strip_pad()

    return q, r


def get_quotient(r: Integer, y: Integer) -> Integer:
    q_prime = 0
    y_prime = Integer([0], y.is_negative, y.radix)

    for i in range(1, r.radix):
        y_prime = add(y_prime, y)

        if not subtract(r, y_prime).is_negative:
            q_prime = i
        else:
            break

    return q_prime



# Remove when multiplication is finished
import string

digs = string.digits + string.ascii_letters


def multiply(x: Integer, y: Integer) -> Integer:
    result = int(x.to_string(), x.radix) * int(y.to_string(), y.radix)

    return Integer.from_string(int2base(result, x.radix), x.radix)


def int2base(x, base):
    if x < 0:
        sign = -1
    elif x == 0:
        return digs[0]
    else:
        sign = 1

    x *= sign
    digits = []

    while x:
        digits.append(digs[int(x % base)])
        x = x // base

    if sign < 0:
        digits.append("-")

    digits.reverse()

    return "".join(digits)
