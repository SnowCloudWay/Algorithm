import sys

if __name__ == '__main__':
    N, M = map(int, sys.stdin.readline().split())
    d = {}

    for i in range(N):
        d[str(i+1)] = sys.stdin.readline().strip()

    r_d = dict(map(reversed,d.items()))

    for _ in range(M):
        s = sys.stdin.readline().strip()

        if s in d.keys():
            print(d.get(s))
        else:
            print(r_d.get(s))