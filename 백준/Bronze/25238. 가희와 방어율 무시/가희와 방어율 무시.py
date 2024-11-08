import sys
input = sys.stdin.readline

a, b = map(int, input().split())
sys.stdout.write("0" if a - ((a * b) / 100) >= 100 else "1")