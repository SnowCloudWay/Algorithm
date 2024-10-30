import sys
input = sys.stdin.readline

n = int(input())
nums = set(map(int, input().split()))

sys.stdout.write(' '.join(map(str, sorted(nums))))