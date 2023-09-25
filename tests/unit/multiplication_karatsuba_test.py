from src.integer import Integer
from src.multiplication import multiplication_karatsuba

def test_is_negative():
	x = Integer.from_string("5", 10)
	y = Integer.from_string("-123", 10)

	result = multiplication_karatsuba(x, y)

	assert result.is_negative

def test_is_positive1():
	x = Integer.from_string("27", 10)
	y = Integer.from_string("15", 10)

	result = multiplication_karatsuba(x, y)

	assert not result.is_negative

def test_is_positive2():
	x = Integer.from_string("-20", 3)
	y = Integer.from_string("-12", 3)

	result = multiplication_karatsuba(x, y)

	assert not result.is_negative

def test_val_b10():
	x = Integer.from_string("378469", 10)
	y = Integer.from_string("9589", 10)

	result = multiplication_karatsuba(x, y)

	assert "3629139241" == result.to_string()

def test_val_b3():
	x = Integer.from_string("2102", 3)
	y = Integer.from_string("121110210", 3)

	result = multiplication_karatsuba(x, y)

	assert "1110122202120" == result.to_string()

def test_val_b16():
	x = Integer.from_string("58E0B", 16)
	y = Integer.from_string("48AF6D9", 16)

	result = multiplication_karatsuba(x, y)

	assert "193C1921F953" == result.to_string()

def test_zero():
	x = Integer.from_string("0", 13)
	y = Integer.from_string("345B8A", 13)

	result = multiplication_karatsuba(x, y)

	assert "0" == result.to_string()

