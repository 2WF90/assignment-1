from src.integer import Integer
from src.basic_arithmetic import add, subtract


# Implementation of Algorithm 1.6 for long division from the lecture notes
def divide(x: Integer, y: Integer) -> tuple[Integer, Integer]:
    # Determine the sign of the result
    result_is_negative = x.is_negative ^ y.is_negative

    # Work with absolute values for division
    x = x.make_absolute()
    y = y.make_absolute()

    # Check for division by zero
    if y.strip_pad().exponents == [0]:
        raise ZeroDivisionError()

    # Initialize variables for quotient and remainder
    r = x  # step 1.1
    k = len(x) - len(y) + 1  # step 1.2
    q = [0] * k

    # Perform the long division
    for i in range(k - 1, -1, -1):
        # Calculate the next quotient digit
        b_i_y = Integer([0] * i + y.exponents, y.is_negative, y.radix)
        q[i] = get_quotient(r, b_i_y)  # step 2.2

        # Update the remainder
        r = subtract(
            r, multiply(Integer([q[i]], False, y.radix), b_i_y)
        )  # step 2.3

    # Create the quotient as an Integer, adjusting the sign, and removing leading zeros
    q = Integer(q, result_is_negative, x.radix).strip_pad()  # step 3.1

    return q, r  # step 3.2

""" The algorithm for getting the quotient digit q_i.
    As y is being passed multiplied by b^i, we know that y is of the same length as r.
    Therefore the for loop will have to run at most r.radix times."""
def get_quotient(r: Integer, y: Integer) -> Integer:
    q_prime = 0
    y_prime = Integer([0], y.is_negative, y.radix)

    for i in range(1, r.radix):
        # Incrementally build a divisor
        y_prime = add(y_prime, y)

        # Check if the current divisor is less than or equal to the remainder
        if not subtract(r, y_prime).is_negative:
            q_prime = i
        else:
            break

    return q_prime



