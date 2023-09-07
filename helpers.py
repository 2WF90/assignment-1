REPRESENTATIONS = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6",
                   7: "7", 8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
KEYS = {v: k for k, v in REPRESENTATIONS.items()}


def get_representation(x: int) -> str:
    return REPRESENTATIONS[x].upper()


def get_key(x: str) -> int:
    return KEYS[x.lower()]


def remove_leading_zeros(x: str) -> str:
    x_stripped = x.lstrip("0")

    if x_stripped == "":
        return "0"

    return x_stripped


def is_positive(x: str) -> bool:
    x_stripped = remove_leading_zeros(x)

    if x_stripped == "0":
        return False

    return not x_stripped.startswith("-")


def is_at_least_zero(x: str) -> bool:
    return not x.startswith("-")


def absolute(x: str) -> str:
    return x[1:] if x[0] == "-" else x


def get_length(x: str) -> int:
    x_absolute = absolute(x)

    return len(remove_leading_zeros(x_absolute))


def radix_to_decimal(radix: int, x: str) -> int:
    is_negative = not is_at_least_zero(x)
    x_absolute = absolute(x)

    decimal = 0

    for i in range(len(x_absolute)):
        decimal += get_key(x_absolute[len(x_absolute) - 1 - i]) * radix ** i

    return -decimal if is_negative else decimal
