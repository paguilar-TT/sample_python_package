class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y


if __name__ == "__main__":
    calc = Calculator()
    print("-- Add --")
    expected = 5
    actual = calc.add(2, 3)
    print("calc.add(2, 3): {0}".format(actual))
    assert expected == actual, "Add Result is wrong. {0} != {1}".format(
        expected, actual)

    print("-- Subtract --")
    expected = -1
    actual = calc.subtract(2, 3)
    print("calc.subtract(2, 3): {0}".format(expected))
    assert expected == actual, "subtract Result is wrong. {0} != {1}".format(
        expected, actual)

    print("-- Multiply --")
    expected = 6
    actual = calc.multiply(2, 3)
    print("calc.multiply(2, 3): {0}".format(expected))
    assert expected == actual, "Multiply Result is wrong. {0} != {1}".format(
        expected, actual)

    print("-- Divide --")
    expected = 3
    actual = calc.divide(6, 2)
    print("calc.divide(6, 2): {0}".format(expected))
    assert expected == actual, "Multiply Result is wrong. {0} != {1}".format(
        expected, actual)
