import sys
input = sys.stdin.readline

N = int(input())

pasta = set(input().split())
hyunbin = set(input().split())
print("".join(pasta - hyunbin))