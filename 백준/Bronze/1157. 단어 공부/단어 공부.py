import sys

if __name__ == '__main__':
    a = sys.stdin.readline().rstrip().upper()
    d = {}
    cnt = 0

    for i in a:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    max_d = [k for k, v in d.items() if max(d.values()) == v]

    if len(max_d) == 1:
        print(''.join(max_d))
    else:
        print('?')