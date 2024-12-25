def fac(x):
    res = 1
    c = 2
    while c <= x:
        res *= c
        c += 1
    return res


def main():
    q = input().split()
    stack = []
    for i in q:
        if i not in '+-*/~!#@':
            stack.append(int(i))
        else:
            match i:
                case '+':
                    stack[-2] = stack[-2] + stack[-1]
                    stack.pop(-1)
                case '-':
                    stack[-2] = stack[-2] - stack[-1]
                    stack.pop(-1)
                case '*':
                    stack[-2] = stack[-2] * stack[-1]
                    stack.pop(-1)
                case '/':
                    stack[-2] = stack[-2] // stack[-1]
                    stack.pop(-1)
                case '~':
                    stack[-1] = -stack[-1]
                case '!':
                    stack[-1] = fac(stack[-1])
                case '#':
                    stack.append(stack[-1])
                case '@':
                    stack[-3], stack[-2], stack[-1] = stack[-2], stack[-1], stack[-3]
    print(stack[0])


if __name__ == "__main__":
    main()
    