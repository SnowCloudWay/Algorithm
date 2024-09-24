if __name__ == '__main__':
    n = int(input())
    nums = []
    for i in range(0, n):
        nums.append(int(input()))
    nums.sort()
    for num in nums:
        print(num)