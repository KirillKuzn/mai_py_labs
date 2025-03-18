def merge(a, b):
    for e in [a, b]:
        if not hasattr(e, "__iter__"):
            raise StopIteration
    
    c = list(a + b)
    if not all(isinstance(x, type(a[0])) for x in c):
        raise TypeError
    
    for e in [a, b]:
        if list(e) != sorted(e):
            raise ValueError
        
    return tuple(sorted(c))