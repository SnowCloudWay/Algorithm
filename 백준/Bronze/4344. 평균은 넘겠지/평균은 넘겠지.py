if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        scores = list(map(int, input().split()))
        cnt = 0

        for j in scores[1:]:
            avg = sum(scores[1:])/scores[0]
            if j > avg:
                cnt += 1

        per = (cnt/scores[0])*100
        print('{0:0.3f}%'.format(per))