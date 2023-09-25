from src.division import *
from src.integer import Integer


def test_general_case():
    x = Integer.from_string("903", 10)
    y = Integer.from_string("14", 10)

    result = divide(x, y)

    assert "64" == result[0].to_string()
    assert "7" == result[1].to_string()

def test_negative_x():
    x = Integer.from_string("-903", 10)
    y = Integer.from_string("14", 10)

    result = divide(x, y)

    assert "-64" == result[0].to_string()
    assert "7" == result[1].to_string()
