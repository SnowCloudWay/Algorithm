import sys

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n, S = map(str, sys.stdin.readline().split())
        S = list(S)
        P = ""
        for i in range(len(S)):
            P += S[i] * int(n)

        print(P)