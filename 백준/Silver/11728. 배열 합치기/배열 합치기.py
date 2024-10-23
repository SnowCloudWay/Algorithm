import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_idx, b_idx = 0, 0

c = a + b
c.sort()
sys.stdout.write(str(' '.join(map(str, c))))