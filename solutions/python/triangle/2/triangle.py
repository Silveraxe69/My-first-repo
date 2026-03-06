def equilateral(sides):
    side1, side2, side3 = sorted(sides)
    return side1 > 0 and side1 + side2 > side3 and side1 == side2 == side3


def isosceles(sides):
    side1, side2, side3 = sorted(sides)
    return side1 > 0 and side1 + side2 > side3 and len(set(sides)) < 3


def scalene(sides):
    side1, side2, side3 = sorted(sides)
    return side1 > 0 and side1 + side2 > side3 and len(set(sides)) == 3
