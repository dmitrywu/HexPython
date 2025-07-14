def is_degenerated(tuple):
    first, second = tuple
    return first == second


def is_vertical(tuple):
    first, second = tuple
    a1, b1 = first
    a2, b2 = second
    return a1 == a2 and b1 != b2


def is_horizontal(tuple):
    first, second = tuple
    a1, b1 = first
    a2, b2 = second
    return b1 == b2 and a1 != a2


def is_inclined(tuple):
    first, second = tuple
    a1, b1 = first
    a2, b2 = second
    return (a1 != a2) and (b1 != b2)


line1 = (0, 10), (100, 130)
print(is_vertical(line1))  # False
print(is_horizontal(line1))  # False
print(is_degenerated(line1))  # False
print(is_inclined(line1))  # True
line2 = (42, 1), (42, 2)
print(is_vertical(line2))  # True
line3 = (100, 50), (200, 50)
print(is_horizontal(line3))  # True
