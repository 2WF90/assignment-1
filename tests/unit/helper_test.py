from helpers import *


def test_keys():
    assert 14 == KEYS["e"]


def test_is_positive():
    assert is_positive("AB894F")


def test_zero_is_not_positive():
    assert not is_positive("0000")


def test_is_not_positive():
    assert not is_positive("-AB894F")


def test_is_at_least_zero():
    assert is_at_least_zero("AB894F")


def test_zero_is_not_at_least_zero():
    assert is_at_least_zero("0000")


def test_is_not_at_least_zero():
    assert not is_at_least_zero("-AB894F")


def test_remove_leading_zeros():
    assert "1" == remove_leading_zeros("0000001")


def test_remove_leading_zeros_empty():
    assert "0" == remove_leading_zeros("0000000")


def test_length():
    assert 5 == get_length("-0091234")


def test_radix_to_decimal():
    assert 238 == radix_to_decimal(16, "EE")
    assert 26354567345569 == radix_to_decimal(7, "5360024514161461")
    assert 42 == radix_to_decimal(2, "101010")
