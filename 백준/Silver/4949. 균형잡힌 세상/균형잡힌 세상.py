import sys

if __name__ == '__main__':
    while True:
        l = sys.stdin.readline().rstrip()
        s = []
        balance = True
        if l == '.': break
        for i in l:
            if i in '([':
                s.append(i)
            elif i == ')':
                if not s or s[-1] != '(':
                    balance = False
                    break
                s.pop()
            elif i == ']':
                if not s or s[-1] != '[':
                    balance = False
                    break
                s.pop()
        if not s and balance:
            print("yes")
        else:
            print("no")