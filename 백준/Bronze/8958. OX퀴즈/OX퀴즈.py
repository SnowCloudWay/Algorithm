if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        ox = list(input())
        score = 0
        total_score = 0
        for i in ox:
            if i == "X":
                score = 0
            elif i == "O":
                score += 1
                total_score += score
        print(total_score)