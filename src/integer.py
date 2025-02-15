from typing import Self
from src.helpers import *


class Integer:
    def __init__(self, exponents: list[int], is_negative: bool = False, radix: int = 10):
        self.exponents = exponents
        self.is_negative = is_negative
        self.radix = radix

    def __len__(self) -> int:
        return len(self.exponents)

    def __getitem__(self, key) -> int:
        return self.exponents[key]

    def from_string(value: str, radix: int) -> Self:
        return Integer(
            [get_key(digit) for digit in absolute(value)][::-1],
            not is_at_least_zero(value),
            radix,
        )

    def to_string(self) -> str:
        if len(self.exponents) == 0:
            return None

        return ("-" if self.is_negative else "") + "".join(
            [get_representation(exponent) for exponent in self.exponents[::-1]],
        )

    def divide_by_radix(self, power: int) -> Self:
        if len(self.exponents) == 0:
            return Integer([], False, self.radix)

        exponents = self.exponents.copy()

        if power >= len(exponents):
            return Integer([0], False, self.radix)

        for _ in range(power):  # remove i digits from the front
            exponents.pop(0)

        if len(exponents) == 0:
            return Integer([0], False, self.radix)

        return Integer(exponents, self.is_negative, self.radix)

    def modulus_radix(self, power: int) -> Self:
        from src.basic_arithmetic import add

        if len(self.exponents) == 0:
            return Integer([], False, self.radix)

        exponents = self.exponents.copy()

        if power + 1>= len(exponents):
            return Integer(exponents.copy(), self.is_negative, self.radix)

        for _ in range(power):  # remove i digits from the front
            exponents.pop()

        result = Integer(exponents, self.is_negative, self.radix)

        if self.is_negative:
            return add(result, Integer([0] * (power + 1) + [1], False, self.radix))

        return result

    def pad_n(self, n: int) -> Self:
        exponents = self.exponents + [0] * n

        return Integer(exponents, self.is_negative, self.radix)

    def pad_back(self, n: int) -> Self:
        exponents = [0] * n + self.exponents

        return Integer(exponents, self.is_negative, self.radix)

    def pad(self, pad_length: int) -> Self:
        exponents = self.exponents + [0] * (pad_length - len(self.exponents))

        return Integer(exponents, self.is_negative, self.radix)

    def strip_pad(self) -> Self:
        exponents = self.exponents.copy()
        while len(exponents) > 1 and exponents[-1] == 0:
            exponents.pop()

        return Integer(exponents, self.is_negative, self.radix)

    def make_absolute(self) -> Self:
        return Integer(self.exponents.copy(), False, self.radix)

    def set_negative(self) -> Self:
        return Integer(self.exponents.copy(), True, self.radix)
