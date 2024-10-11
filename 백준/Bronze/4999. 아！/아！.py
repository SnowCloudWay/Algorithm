import sys

a = sys.stdin.readline().rstrip()
b = sys.stdin.readline().rstrip()

if len(a) >= len(b):
    sys.stdout.write("go")
else:
    sys.stdout.write("no")