class SimpleNumber:
    """The class is a basic implementation of a number class in Python"""

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other

    def __sub__(self, other):
        return self.value - other

    def __mul__(self, other):
        return self.value * other

    def __truediv__(self, other):
        return self.value / other
