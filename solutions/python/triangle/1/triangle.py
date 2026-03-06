def equilateral(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c and a == b == c


def isosceles(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c and len(set(sides)) < 3


def scalene(sides):
    a, b, c = sorted(sides)
    return a > 0 and a + b > c and a != b != c != a
