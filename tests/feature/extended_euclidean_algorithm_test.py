from .assert_answer import assert_exercise


def test_realistic_exercise_1():
    assert_exercise("realistic", 8)


def test_realistic_exercise_2():
    assert_exercise("realistic", 11)


def test_simple_exercise_1():
    assert_exercise("simple", 4)


def test_simple_exercise_2():
    assert_exercise("simple", 5)
