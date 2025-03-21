if __name__ == '__main__':
    n = int(input())
    num = list(map(int, input().split()))
    result = []

    for i in range(n):
        result.insert(i-num[i], i+1)

    for v in result:
        print(v, end=" ")