p = int(input())
v = int(input())
t = int(input())
if p > max(v, t):
    print(f"{'Петя': ^24}")
    if v > t:
        print(f"{'Вася': ^8}")
        print(f"{'Толя': >22}")
    else:
        print(f"{'Толя': ^8}")
        print(f"{'Вася': >22}")
if v > max(p, t):
    print(f"{'Вася': ^24}")
    if p > t:
        print(f"{'Петя': ^8}")
        print(f"{'Толя': >22}")
    else:
        print(f"{'Толя': ^8}")
        print(f"{'Петя': >22}")
if t > max(v, p):
    print(f"{'Толя': ^24}")
    if v > p:
        print(f"{'Вася': ^8}")
        print(f"{'Петя': >22}")
    else:
        print(f"{'Петя': ^8}")
        print(f"{'Вася': >22}")      
print(f"{'II': ^8}{'I': ^8}{'III': ^8}")    