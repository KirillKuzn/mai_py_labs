string = input()
ans = ''.join([word[0].upper() for word in string.split()])
print(ans)