from src.helpers import *
from src.integer import *


def test_is_negative():
    x = Integer.from_string("-AB894F")

    assert True == x.is_negative


def test_exponents_value():
    x = Integer.from_string("-AB894F")

    assert [15, 4, 9, 8, 11, 10] == x.exponents


def test_to_string():
    x = Integer.from_string("AB894F")

    assert "AB894F" == x.to_string()


def test_negative_to_string():
    x = Integer.from_string("-AB894F")

    assert "-AB894F" == x.to_string()


def test_with_padding():
    x = Integer.from_string("-AB894F")

    assert "-0000AB894F" == x.with_padding(10).to_string()
