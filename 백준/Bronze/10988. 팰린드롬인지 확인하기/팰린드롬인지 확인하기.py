import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    if word == word[::-1]:
        print(1)
    else:
        print(0)