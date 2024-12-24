n = int(input())
m = int(input())
t = int(input())
tn = t // 60
tm = t % 60
n += tn
m += tm
if m >= 60:
    n += m // 60
    m = m % 60
if n >= 24:
    n = n % 24
if n >= 10 and m >= 10:
    print(f"{n}:{m}")
elif n >= 10 and m < 10:
    print(f"{n}:0{m}")
elif n < 10 and m >= 10:
    print(f"0{n}:{m}")
else:
    print(f"0{n}:0{m}")
