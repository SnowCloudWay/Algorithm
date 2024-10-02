if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        tc = input()
        stack = []

        for i in tc:
            if i == '(':
                stack.append(i)
            elif i == ')':
                if '(' in stack:
                    stack.pop()
                else:
                    stack.append(i)
                    break
        if stack:
            print("NO")
        else:
            print("YES")