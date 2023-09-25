from src.integer import Integer


# Implementation of Algorithm 1.2 for addition from the lecture notes.
def add(x: Integer, y: Integer) -> Integer:
    # handle negative numbers by performing subtraction
    if x.is_negative and not y.is_negative:
        return subtract(y, x.make_absolute())

    if y.is_negative and not x.is_negative:
        return subtract(x, y.make_absolute())

    # find the maximum length to ensure proper alignment for addition
    max_length = max(len(x), len(y))

    # pad integers with zeros to make them compatible for addition
    padded_x = x.pad(max_length)
    padded_y = y.pad(max_length)

    result = [0] * max_length
    carry = 0

    # perform addition digit by digit, considering overflow
    for i in range(max_length):
        result[i] = padded_x[i] + padded_y[i] + carry

        # adjust for radix (base) if necessary
        if result[i] >= x.radix:
            result[i] -= x.radix
            carry = 1
        else:
            carry = 0

    # if there's a carry after the loop, append it to the result
    if carry == 1:
        result.append(carry)

    # create and return a new Integer object with the result
    return Integer(result, x.is_negative, x.radix)


# Implementation of Algorithm 1.3 for subtraction from the lecture notes.
def subtract(x: Integer, y: Integer) -> Integer:
    # handle cases where both x and y are negative
    if x.is_negative and y.is_negative:
        # subtract x from y by taking the absolute values
        return subtract(y.make_absolute(), x.make_absolute())

    # handle cases where x is negative
    if x.is_negative:
        # subtract y from the absolute value of x and get the result as negative
        return add(x.make_absolute(), y).set_negative()

    # handle cases where y is negative
    if y.is_negative:
        # add x and the absolute value of y
        return add(x, y.make_absolute())

    # find the maximum length to ensure proper alignment for subtraction
    max_length = max(len(x), len(y))

    # pad integers with zeros to make them compatible for subtraction
    padded_x = x.pad(max_length)
    padded_y = y.pad(max_length)

    # compare digits from left to right to determine which number is greater
    for i in range(max_length - 1, -1, -1):
        if padded_x[i] > padded_y[i]:
            break
        if padded_x[i] < padded_y[i]:
            # if y is greater, subtract x from y and get the result as negative
            return subtract(y, x).set_negative()

    result = [0] * max_length
    carry = 0

    # perform subtraction digit by digit, considering underflow
    for i in range(max_length):
        result[i] = padded_x[i] - padded_y[i] - carry

        # adjust for negative results
        if result[i] < 0:
            result[i] += x.radix
            carry = 1
        else:
            carry = 0

    # return the result as a new Integer object, removing any leading zeros
    return Integer(result, x.is_negative, x.radix).strip_pad()
