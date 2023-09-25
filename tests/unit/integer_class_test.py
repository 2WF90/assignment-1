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


def test_divide_by_radix():
    x = Integer.from_string("-900", 16)

    assert "-9" == x.divide_by_radix(2).to_string()

def test_divide_by_radix2():
    x = Integer.from_string("EEFF", 16)

    assert "EEF" == x.divide_by_radix(1).to_string()

def test_divide_by_radix2():
    x = Integer.from_string("140", 10)

    assert "0" == x.divide_by_radix(3).to_string()


def test_modulus_radix():
    x = Integer.from_string("911", 16)

    assert "11" == x.modulus_radix(1).to_string()

def test_modulus_radix():
    x = Integer.from_string("-911", 10)

    assert "89" == x.modulus_radix(1).to_string()
