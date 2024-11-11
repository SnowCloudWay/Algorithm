import sys
input = sys.stdin.readline

n, m = map(int, input().split())
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

setA -= setB
setA = sorted(setA)

sys.stdout.write(str(len(setA))+'\n')
if len(setA) != 0:
    sys.stdout.write(' '.join(map(str, setA)))