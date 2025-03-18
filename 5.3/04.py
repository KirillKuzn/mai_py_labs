def only_positive_even_sum(a, b):
    for e in [a, b]:
        if not (isinstance(e, int)):
            raise TypeError
    for e in [a, b]:
        if not (e > 0 and e % 2 == 0):
            raise ValueError
    return a + b