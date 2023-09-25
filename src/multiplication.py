from src.integer import Integer
from src.basic_arithmetic import add, subtract
from src.reduction import reduce

#----------------------------------------------------------------
# KARATSUBA
#----------------------------------------------------------------

# Gateway to karatsuba, does negativity and length overhead checks
# param: x, any Integer
# param: y, any Integer
# return x * y, Integer
def multiplication_karatsuba(x: Integer, y: Integer) -> Integer:
    max_length = max(len(x), len(y))
    x = x.pad(max_length)
    y = y.pad(max_length)

    if x.is_negative ^ y.is_negative:
        result = karatsuba(x, y).set_negative().strip_pad()
    else:
        result = karatsuba(x, y).strip_pad()

    if len(result) == 0:
        result.pad_n(1)

    return result

# Karatsuba algorithm, calculates multiplication of 2 integers
# param: x, Integer
# param: y, Integer
# length of x and y must be the same
# return x * y, Integer
def karatsuba(x: Integer, y: Integer) -> Integer:
    n = len(x)

    if len(y) != n:
        raise ValueError("Somewhere something is fucked")

    # Base case:
    if n == 1:
        m = x[0] * y[0]

        return Integer([m % x.radix, m // x.radix], False, x.radix)

    # Step:
    # Make list lenght even
    if n & 1:
        x = x.pad_n(1)
        y = y.pad_n(1)
        n = n + 1

    halfN = n >> 1

    # Devide number in 2 parts
    Xl = Integer(x[halfN:], False, x.radix)
    Xs = Integer(x[:halfN], False, x.radix)
    Xm = add(Xl, Xs)

    Yl = Integer(y[halfN:], False, x.radix)
    Ys = Integer(y[:halfN], False, x.radix)
    Ym = add(Yl, Ys)

    # Addition lenght checking
    xmLen = len(Xm)
    ymLen = len(Ym)
    if xmLen > ymLen:
        Ym = Ym.pad_n(1)
    elif ymLen > xmLen:
        Xm = Xm.pad_n(1)

    # Recurse on all 3 parts
    XlYl = karatsuba(Xl, Yl)
    XsYs = karatsuba(Xs, Ys)
    XmYm = karatsuba(Xm, Ym)

    # Compute mid and shift digits
    XmYm = subtract(subtract(XmYm, XlYl), XsYs)
    XmYm = XmYm.pad_back(halfN)
    XlYl = XlYl.pad_back(n)

    return add(add(XlYl, XmYm), XsYs)

#----------------------------------------------------------------
# PRIMARY SHOOL METHOD
#----------------------------------------------------------------

def multiplication_primary(x: Integer, y: Integer) -> Integer:
    result = [0] * (len(x) + len(y))
    carry = 0

    for i in range(len(x)):
        for j in range(len(y)):
            r = x[i] * y[j] + carry + result[i + j]
            result[i + j] = r % x.radix
            carry = r // x.radix

        result[i + len(y)] += carry
        carry = 0

    sign = x.is_negative ^ y.is_negative

    return Integer(result, sign, x.radix).strip_pad()


#----------------------------------------------------------------
# MODULAR MULTIPLICATION USING KARATSUBA
#----------------------------------------------------------------
def mod_multiplication(x: Integer, y: Integer, modulus: Integer) -> Integer:
    if (modulus.strip_pad().exponents == [0]):
        return Integer([], False, x.radix)


    y = reduce(y, modulus)
    x = reduce(x, modulus)

    return reduce(multiplication_karatsuba(x, y), modulus)
