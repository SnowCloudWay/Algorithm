if __name__ == '__main__':
    n = int(input())
    results = []
    cnt = 1
    for i in range(0, n):
        a, b = map(int, input().split())
        results.append(a+b)
    for result in results:
        print('Case #{}: {}'.format(cnt, result))
        cnt += 1