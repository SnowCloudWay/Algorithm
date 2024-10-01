if __name__ == '__main__':
    l = list(input())
    s = []

    for i in l:
        if i not in "+-*/":
            s.append(int(i))
        else:
            a = s.pop()
            b = s.pop()
            if i == '+': s.append(b + a)
            if i == '-': s.append(b - a)
            if i == '*': s.append(b * a)
            if i == '/': s.append(b // a)

    print(s.pop())