from euclidian.int_euclidian import division_count, long_division
from add.int_addition import addition
from solver.solve import solve


def test_assert_primary_mult():
    assert {'answer': '-484'} == solve(
        {
            "type": "integer_arithmetic",
            "operation": "multiplication_primary",
            "radix": 10,
            "x": "-22",
            "y": "22",
            "points": 0.5
        }
    )

    assert {'answer': '-100011110000000010001101010010'} == solve(
        {
            "type": "integer_arithmetic",
            "operation": "multiplication_primary",
            "radix": 2,
            "x": "-10001011011001",
            "y": "10000011010100010",
            "points": 0.5
        }
    )


def test_division():
    assert "110" == long_division(10, "1210", "11")[0]


def test_division_binary():
    assert "1000" == long_division(2, "10011100001111", "10011010000")[0]


def test_division_binary2():
    assert "111" == long_division(
        2, "1010100000000000000000000000000000000000000000000000", "1100000000000000000000000000000000000000000000000")[0]


def test_division_count():
    assert "5" == division_count(10, "55", "10")[0]
    assert "6" == division_count(10, "912", "140")[0]
    assert "6" == division_count(8, "1620", "214")[0]
    assert "6" == division_count(16, "390", "8C")[0]


def test_addition():
    assert "231" == addition(10, "109", "122")
    assert "11001011011110" == addition(2, "11001001100100", "1111010")
    assert "347" == addition(8, "155", "172")
    assert "E7" == addition(16, "6D", "7A")
