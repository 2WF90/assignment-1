from src.integer import Integer


def add(x: Integer, y: Integer) -> Integer:
    if x.is_negative and not y.is_negative:
        return subtract(y, x.make_absolute())

    if y.is_negative and not x.is_negative:
        return subtract(x, y.make_absolute())

    max_length = max(len(x), len(y))

    padded_x = x.pad(max_length)
    padded_y = y.pad(max_length)

    result = [0] * max_length
    carry = 0

    for i in range(max_length):
        result[i] = padded_x.exponents[i] + padded_y.exponents[i] + carry

        if result[i] >= x.radix:
            result[i] -= x.radix
            carry = 1

        else:
            carry = 0

    if carry == 1:
        result.append(carry)

    return Integer(result, x.is_negative)


def subtract(x: Integer, y: Integer) -> Integer:
    # TODO ask if we also should account for when x < y

    if x.is_negative and y.is_negative:
        return subtract(y.make_absolute(), x.make_absolute())

    if x.is_negative:
        return add(x.make_absolute(), y).set_negative()

    if y.is_negative:
        return add(x, y.make_absolute())

    max_length = max(len(x), len(y))

    padded_x = x.pad(max_length)
    padded_y = y.pad(max_length)

    result = [0] * max_length
    carry = 0

    for i in range(max_length):
        result[i] = padded_x.exponents[i] - padded_y.exponents[i] - carry

        if result[i] < 0:
            result[i] += x.radix
            carry = 1
        else:
            carry = 0

    return Integer(result, x.is_negative).strip_pad()