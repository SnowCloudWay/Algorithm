import sys
input = sys.stdin.readline

def solution(x, y, n):
    global a, b, c
    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                solution(x, y, n//3)
                solution(x, y+n//3, n//3)
                solution(x, y+2*n//3, n//3)
                solution(x+n//3, y, n//3)
                solution(x+n//3, y+n//3, n//3)
                solution(x+n//3, y+2*n//3, n//3)
                solution(x+2*n//3, y, n//3)
                solution(x+2*n//3, y+n//3, n//3)
                solution(x+2*n//3, y+2*n//3, n//3)
                return
    if num == -1:
        a += 1
    elif num == 0:
        b += 1
    else:
        c += 1


if __name__ == '__main__':
    a, b, c = 0, 0, 0
    n = int(input())
    paper = [list(map(int, input().split())) for _ in range(n)]

    solution(0, 0, n)
    sys.stdout.write(str(a) + "\n" + str(b) + "\n" + str(c))