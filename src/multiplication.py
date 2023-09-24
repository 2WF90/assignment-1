from integer import Integer
from basic_arithmetic import add, subtract

# Gateway to karatsuba, does negativity overhead checks
def multiplication(a: Integer, b: Integer) -> Integer:
	if a.is_negative ^ b.is_negative:
		return karastuba(a, b).set_negative()

	return karastuba(a, b)


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
	XlYl = karastuba(Xl, Yl)
	XsYs = karastuba(Xs, Ys)
	XmYm = karastuba(Xm, Ym)

	XmYm = subtract(subtract(XmYm, XlYl), XsYs).pad_back(halfN)
	XlYl.pad_back(n)

	return add(add(XlYl, XmYm), XsYs)


if __name__ == "__main__":
	a = Integer([1, 2, 3, 4, 5], False, 10)
	b = Integer([1, 2, 3, 4, 5], False, 10)

	print(multiplication(a, b).exponents)