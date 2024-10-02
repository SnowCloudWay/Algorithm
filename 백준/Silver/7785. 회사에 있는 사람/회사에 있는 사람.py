import sys

if __name__ == '__main__':
    n = int(input())

    d = {}
    for _ in range(n):
        name, state = map(str, sys.stdin.readline().split())
        if state == "enter":
            d[name] = state
        elif state == "leave":
            del d[name]

    print('\n'.join(sorted(d.keys(), reverse=True)))