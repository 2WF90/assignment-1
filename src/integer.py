from src.helpers import *
from typing import Self

class Integer:
    def __init__(self, exponents: list[int], is_negative: bool = False):
        self.exponents = exponents
        self.is_negative = is_negative

    def __len__(self):
        return len(self.exponents)

    def from_string(value: str) -> Self:
        return Integer(
            [get_key(digit) for digit in absolute(value)][::-1],
            not is_at_least_zero(value),
        )

    def to_string(self) -> str:
        return ("-" if self.is_negative else "") + "".join(
            [get_representation(exponent) for exponent in self.exponents[::-1]]
        )

    def with_padding(self, length: int) -> Self:
        return Integer(self.exponents + [0] * (length - len(self.exponents)), self.is_negative)
