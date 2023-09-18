from typing import Self
from src.helpers import *


class Integer:
    def __init__(self, exponents: list[int], is_negative: bool = False, radix: int = 10):
        self.exponents = exponents
        self.is_negative = is_negative
        self.radix = radix

    def __len__(self):
        return len(self.exponents)

    def from_string(value: str, radix: int) -> Self:
        return Integer(
            [get_key(digit) for digit in absolute(value)][::-1],
            not is_at_least_zero(value),
            radix,
        )

    def to_string(self) -> str:
        return ("-" if self.is_negative else "") + "".join(
            [get_representation(exponent) for exponent in self.exponents[::-1]]
        )

    def pad(self, pad_length: int) -> Self:
        self.exponents += [0] * (pad_length - len(self.exponents))

        return self

    def strip_pad(self) -> Self:
        while self.exponents and self.exponents[-1] == 0:
            self.exponents.pop()

        return self

    def make_absolute(self) -> Self:
        self.is_negative = False

        return self

    def set_negative(self) -> Self:
        self.is_negative = True

        return self
