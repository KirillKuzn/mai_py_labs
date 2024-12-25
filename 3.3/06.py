text = input()
ans = {i: text.lower().count(i) for i in ''.join(filter(str.isalpha, sorted(text.lower())))}
print(ans)