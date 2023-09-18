from src.basic_arithmetic import add, subtract
from src.integer import Integer


def test_is_negative2():
    x = Integer.from_string("10", 10)
    y = Integer.from_string("-9", 10)

    result = add(x, y)

    assert "1" == result.to_string()
