import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    sys.stdout.write("long " * (N // 4) + "int")