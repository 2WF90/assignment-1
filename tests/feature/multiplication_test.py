from .assert_answer import assert_exercise


def test_realistic_exercise_1():
    assert_exercise("realistic", 12)


def test_realistic_exercise_2():
    assert_exercise("realistic", 13)


def test_simple_exercise_1():
    assert_exercise("simple", 10)


def test_simple_exercise_2():
    assert_exercise("simple", 11)
