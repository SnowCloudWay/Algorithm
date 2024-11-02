import sys
input = sys.stdin.readline

n = int(input())
for i in range(1, n + 1):
    sys.stdout.write("Hello World, Judge {}!\n".format(i))