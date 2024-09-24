if __name__ == '__main__':
    n = int(input())
    score = list(map(int, input().split()))
    max_score = 0

    for i in score:
        max_score = max(max_score, i)

    false_score = score
    average_score = 0

    for i in range(n):
        false_score[i] = score[i] / max_score * 100
        average_score += false_score[i]

    average_score = average_score / n

    print(average_score)