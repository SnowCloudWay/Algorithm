import sys

if __name__ == '__main__':
    a = sys.stdin.readline().rstrip()
    b = list(sys.stdin.readline().rstrip())
    n = len(b)
    s = []

    for i in a:
        s.append(i)
        if s[-n:] == b:
            for _ in range(n):
                s.pop()

    if len(s) != 0:
        print(''.join(s))
    else:
        print('FRULA')