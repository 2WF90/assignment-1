from src.basic_arithmetic import add, subtract
from src.integer import Integer


def test_subtract_leading_term_y_larger_than_x():
    x = Integer.from_string("9", 10)
    y = Integer.from_string("10", 10)

    result = subtract(x, y)

    assert "-1" == result.to_string()


def test_subtract_last_term_y_larger_than_x():
    x = Integer.from_string("300", 10)
    y = Integer.from_string("301", 10)

    result = subtract(x, y)

    assert "-1" == result.to_string()



