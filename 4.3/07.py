def same_type(f):
    def dec(*args):
        if all([type(i) is type(args[0]) for i in args]):
            return f(*args)
        print("Обнаружены различные типы данных")
    return dec


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
