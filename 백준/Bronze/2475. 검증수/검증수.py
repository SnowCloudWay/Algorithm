if __name__ == '__main__':
    a, b, c, d, e = map(int, input().split())
    total_sum = (a*a) + (b*b) + (c*c) + (d*d) + (e*e)
    result = total_sum % 10
    print(result)