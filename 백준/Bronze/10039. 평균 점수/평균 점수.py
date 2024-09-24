if __name__ == '__main__':
    total = 0
    for i in range(0, 5):
        score = int(input())
        if score < 40:
            score = 40
        total += score
    avg_score = total / 5
    print(int(avg_score))