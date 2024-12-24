s1 = input()
s2 = input()
s3 = input()
s = []
if 'зайка' in s1:
    s.append(s1)
if 'зайка' in s2:
    s.append(s2)
if 'зайка' in s3:
    s.append(s3)
print(min(s), len(min(s)))