from integer import Integer
from basic_arithmetic import add, subtract

# Gateway to karatsuba, does negativity and length overhead checks
def multiplication(x: Integer, y: Integer) -> Integer:
    max_length = max(len(x), len(y))
    x.pad(max_length)
    y.pad(max_length)

    if x.is_negative ^ y.is_negative:
        return karatsuba(x, y).set_negative().strip_pad()

    return karatsuba(x, y).strip_pad()

# Karatsuba algorithm, calculates multiplication of 2 integers
def karatsuba(x: Integer, y: Integer) -> Integer:
    n = len(x)

    if len(y) != n:
        raise ValueError("Somewhere something is fucked")

    # Base case:
    if n == 1:
        m = x[0] * y[0]
        print(x[0], y[0], m)

        return Integer([m % x.radix, m // x.radix], False, x.radix)

    # Step:
    # Make list lenght even
    if n & 1: 
        x.pad_n(1)
        y.pad_n(1)
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
        Ym.pad_n(1)
    elif ymLen > xmLen:
        Xm.pad_n(1)

    # Recurse on all 3 parts
    XlYl = karatsuba(Xl, Yl)
    XsYs = karatsuba(Xs, Ys)
    XmYm = karatsuba(Xm, Ym)

    # Compute mid and shift digits
    XmYm = subtract(subtract(XmYm, XlYl), XsYs)
    XmYm.pad_back(halfN)
    XlYl.pad_back(n)

    return add(add(XlYl, XmYm), XsYs)


if __name__ == "__main__":
    #a = Integer([1, 2, 3, 4, 5, 6, 7], False, 10)
    #b = Integer([1, 2, 3, 4, 5, 6, 7], False, 10)

    a = Integer([2, 3], False, 10)
    b = Integer([3,4,5,8], False, 10)

    print(multiplication(a, b).exponents)