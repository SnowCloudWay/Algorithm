import sys

if __name__ == '__main__':
    while True:
        num = sys.stdin.readline().rstrip()
        if num == '0': break
        if num == num[::-1]:
            print('yes')
        else:
            print('no')