if __name__ == '__main__':
    n = int(input())
    cnt = 1
    for i in range(0, n):
        a, b = map(int, input().split())
        result = a + b
        print('Case #{}: {} + {} = {}'.format(cnt, a, b, result))
        cnt += 1