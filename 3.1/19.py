def main():
    q = input().split()
    stack = []
    for i in q:
        if i not in '+-*':
            stack.append(int(i))
        else:
            match i:
                case '+':
                    stack[-2] = stack[-2] + stack[-1]
                case '-':
                    stack[-2] = stack[-2] - stack[-1]
                case '*':
                    stack[-2] = stack[-2] * stack[-1]
            stack.pop(-1)
    print(stack[0])


if __name__ == "__main__":
    main()

