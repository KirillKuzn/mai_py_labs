class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a, b, c):
    for e in [a, b, c]:
        if not isinstance(e, (int, float)):
            raise TypeError
    if a == b == c == 0:
        raise InfiniteSolutionsError
    elif a == b == 0:
        raise NoSolutionsError
    d = b ** 2 - 4 * a * c
    if d < 0:
        raise NoSolutionsError
    if d == 0:
        root = -b / (2 * a)
        return (root, root)
    if d >= 0:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return (x2, x1)
    

# print(find_roots(0, 0, 1))
# print(find_roots(1, 2, 1))
# print(find_roots(1, 2, 2))