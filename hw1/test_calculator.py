from Calculator import Calculator

def test_get_last_calculation():
    calc1 = Calculator(10)
    actual = calc1.get_last_calculation()
    expected = 10
    assert actual == expected


def test_default_instantiation():
    calc1 = Calculator()
    actual = calc1.get_last_calculation()
    expected = 0
    assert actual == expected


def test_add_1():
    calc1 = Calculator()
    actual = calc1.add(15)
    expected = 15
    assert actual == expected


def test_add_2():
    # Arrange
    calc1 = Calculator()
    # Act
    actual = calc1.add(1, 2)
    expected = 3
    # Assert
    assert actual == expected


def test_invalid_input_addend1():
    calc1 = Calculator()
    actual = calc1.add("hello", 10)
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_input_addend2():
    calc1 = Calculator()
    actual = calc1.add(1, "goodbye")
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_input_add_both():
    calc1 = Calculator()
    actual = calc1.add("hello", "goodbye")
    expected = "INVALID INPUT"
    assert actual == expected


def test_subtract_1():
    calc1 = Calculator(10)
    actual = calc1.subtract(5)
    expected = 5
    assert actual == expected


def test_subtract_2():
    calc1 = Calculator()
    actual = calc1.subtract(7, 5)
    expected = 2
    assert actual == expected


def test_invalid_input_sub1():
    calc1 = Calculator()
    actual = calc1.subtract("hello", 10)
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_input_sub2():
    calc1 = Calculator()
    actual = calc1.subtract(1, "goodbye")
    expected = "INVALID INPUT"
    assert actual == expected


def test_invalid_input_sub_both():
    calc1 = Calculator()
    actual = calc1.subtract("hello", "goodbye")
    expected = "INVALID INPUT"
    assert actual == expected
