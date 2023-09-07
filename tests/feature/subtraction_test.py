from .assert_answer import assert_exercise


def test_realistic_exercise_1():
    assert_exercise("realistic", 3)


def test_realistic_exercise_2():
    assert_exercise("realistic", 11)


def test_simple_exercise_1():
    assert_exercise("simple", 1)


def test_simple_exercise_2():
    assert_exercise("simple", 9)
