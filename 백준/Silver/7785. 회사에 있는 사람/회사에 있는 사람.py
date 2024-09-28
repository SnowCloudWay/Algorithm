import sys

if __name__ == '__main__':
    n = int(input())

    d = {}
    for _ in range(n):
        name, state = map(str, sys.stdin.readline().split())
        if state == "enter":
            d[name] = state
        else:
            del d[name]

    d = sorted(d.keys(), reverse=True)
    for key in d:
        print(key)