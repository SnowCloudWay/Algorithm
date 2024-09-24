if __name__ == '__main__':
    sub4 = []
    sub2 = []

    for _ in range(4):
        score = int(input())
        sub4.append(score)

    for _ in range(2):
        score = int(input())
        sub2.append(score)

    sub4.sort()
    sub2.sort()

    max_sum = 0
    max_sum += sub4[1] + sub4[2] + sub4[3] + sub2[1]
    print(max_sum)