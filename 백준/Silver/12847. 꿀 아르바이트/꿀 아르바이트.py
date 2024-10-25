import sys
input = sys.stdin.readline

def solution(n, m, money):
    interval_sum = sum(money[:m])
    max_money = interval_sum
    start, end = 0, m

    while end < n:
        interval_sum -= money[start]
        interval_sum += money[end]
        start += 1
        end += 1
        if interval_sum > max_money:
            max_money = interval_sum

    return max_money


n, m = map(int, input().split())
money = list(map(int, input().split()))
sys.stdout.write(str(solution(n, m, money)))