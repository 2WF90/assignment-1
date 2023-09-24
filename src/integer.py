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

    def pad(self, pad_length: int) -> Self:
        exponents = self.exponents + [0] * (pad_length - len(self.exponents))

        return Integer(exponents, self.is_negative, self.radix)

    def strip_pad(self) -> Self:
        while len(self.exponents) > 1 and self.exponents[-1] == 0:
            self.exponents.pop()

        return Integer(self.exponents, self.is_negative, self.radix)

    def make_absolute(self) -> Self:
        return Integer(self.exponents, False, self.radix)

    def set_negative(self) -> Self:
        return Integer(self.exponents, True, self.radix)
