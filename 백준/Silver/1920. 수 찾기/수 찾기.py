import sys

def binary_search(target, data):
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return 1
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return 0

if __name__ == '__main__':
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    f = list(map(int, sys.stdin.readline().split()))

    a.sort()

    for i in f:
        result = binary_search(i, a)
        sys.stdout.write(str(result) + '\n')