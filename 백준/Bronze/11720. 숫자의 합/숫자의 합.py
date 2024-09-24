if __name__ == '__main__':
    n = int(input())
    nums_str = list(input())
    nums = list(map(int, nums_str))
    result = 0

    for i in nums:
        result += i

    print(result)