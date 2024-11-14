import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

dy = [-1, -1, -1, 1, 1, 1, 0, 0]
dx = [-1, 0, 1, -1, 0, 1, -1, 1]

def dfs(y, x):
    visited[y][x] = True
    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < h and 0 <= nx < w:
            if not visited[ny][nx] and matrix[ny][nx]:
                dfs(ny, nx)


if __name__ == '__main__':
    while True:
        w, h = map(int, input().split())
        if w == h == 0:
            break

        matrix = []
        visited = [[False] * w for _ in range(h)]
        cnt = 0

        for _ in range(h):
            matrix.append(list(map(int, input().split())))

        for i in range(h):
            for j in range(w):
                if not visited[i][j] and matrix[i][j]:
                    dfs(i, j)
                    cnt += 1
        sys.stdout.write(str(cnt) + '\n')