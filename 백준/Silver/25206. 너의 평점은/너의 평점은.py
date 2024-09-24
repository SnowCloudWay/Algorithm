if __name__ == '__main__':
    totalScore = 0.0
    totalCredit = 0

    for i in range(0, 20):
        a, b, grades = input().split()
        b = float(b)
        if grades != 'P':
            if grades == 'A+':
                totalScore += b * 4.5
            elif grades == 'A0':
                totalScore += b * 4.0
            elif grades == 'B+':
                totalScore += b * 3.5
            elif grades == 'B0':
                totalScore += b * 3.0
            elif grades == 'C+':
                totalScore += b * 2.5
            elif grades == 'C0':
                totalScore += b * 2.0
            elif grades == 'D+':
                totalScore += b * 1.5
            elif grades == 'D0':
                totalScore += b * 1.0
            elif grades == 'F':
                totalScore += b * 0.0
            totalCredit += b

    avgScore = totalScore / totalCredit
    print(f'{avgScore:.6f}')