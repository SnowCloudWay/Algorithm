import sys
input = sys.stdin.readline

def bs_left(target, data):
    low = 0
    high = len(data) - 1
    result = -1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            result = mid
            high = mid - 1
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return result


n, m = map(int, input().split())
nums = list(map(int, sys.stdin.read().splitlines()))
b = sorted(nums[:n])
d = nums[n:]

for num in d:
    sys.stdout.write(str(bs_left(num, b))+'\n')