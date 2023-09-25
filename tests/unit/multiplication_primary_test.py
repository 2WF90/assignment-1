from src.integer import Integer
from src.multiplication import multiplication_primary

def test_is_negative():
	x = Integer.from_string("-345", 10)
	y = Integer.from_string("45769", 10)

	result = multiplication_primary(x, y)

	assert result.is_negative

def test_is_positive1():
	x = Integer.from_string("34", 10)
	y = Integer.from_string("678", 10)

	result = multiplication_primary(x, y)

	assert not result.is_negative

def test_is_positive2():
	x = Integer.from_string("-3845", 3)
	y = Integer.from_string("-9", 3)

	result = multiplication_primary(x, y)

	assert not result.is_negative

def test_val_b10():
	x = Integer.from_string("8934350", 10)
	y = Integer.from_string("8234", 10)

	result = multiplication_primary(x, y)

	assert "73565437900" == result.to_string()

def test_val_b3():
	x = Integer.from_string("2102", 3)
	y = Integer.from_string("121110210", 3)

	result = multiplication_primary(x, y)

	assert "1110122202120" == result.to_string()

def test_val_b16():
	x = Integer.from_string("58E0B", 16)
	y = Integer.from_string("48AF6D9", 16)

	result = multiplication_primary(x, y)

	assert "193C1921F953" == result.to_string()

def test_zero():
	x = Integer.from_string("43A89B", 13)
	y = Integer.from_string("0", 13)

	result = multiplication_primary(x, y)

	assert "0" == result.to_string()