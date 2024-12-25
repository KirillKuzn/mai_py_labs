def result_accumulator(f):
    queue = []
    
    def dec(*args, method="accumulate", **kwargs):
        queue.append(f(*args, **kwargs))
        if method == "drop":
            res = list(queue)
            queue.clear()
            return res
        return

    return dec
        

@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))