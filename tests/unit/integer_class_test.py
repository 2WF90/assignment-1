from src.helpers import *
from src.integer import *


def test_is_negative():
    x = Integer.from_string("-AB894F", 16)

    assert True == x.is_negative


def test_exponents_value():
    x = Integer.from_string("-AB894F", 16)

    assert [15, 4, 9, 8, 11, 10] == x.exponents


def test_to_string():
    x = Integer.from_string("AB894F", 16)

    assert "AB894F" == x.to_string()


def test_to_string_strip_padding():
    x = Integer.from_string("0000AB894F", 16)

    assert "AB894F" == x.strip_pad().to_string()


def test_negative_to_string():
    x = Integer.from_string("-AB894F", 16)

    assert "-AB894F" == x.to_string()


def test_with_padding():
    x = Integer.from_string("-AB894F", 16)

    assert "-0000AB894F" == x.pad(10).to_string()
