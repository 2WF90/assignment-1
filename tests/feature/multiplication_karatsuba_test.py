from .assert_answer import assert_exercise


def test_realistic_exercise():
    assert_exercise("realistic", 3)


def test_simple_exercise():
    assert_exercise("simple", 3)
