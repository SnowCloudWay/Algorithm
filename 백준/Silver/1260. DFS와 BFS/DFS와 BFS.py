import sys
from collections import deque
input = sys.stdin.readline


def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=" ")
    for i in sorted(graph[v]):
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True
    while que:
        v = que.popleft()
        print(v, end=" ")
        for i in sorted(graph[v]):
            if not visited[i]:
                que.append(i)
                visited[i] = True


if __name__ == '__main__':
    n, m, s = map(int, input().split())
    graph = [[] for _ in range(n+1)]

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    visited = [False] * (n + 1)
    dfs(graph, s, visited)
    print()
    visited = [False] * (n + 1)
    bfs(graph, s, visited)