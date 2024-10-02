import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    time = 0
    for w in word:
        if w in 'ABC':
            time += 3
        elif w in 'DEF':
            time += 4
        elif w in 'GHI':
            time += 5
        elif w in 'JKL':
            time += 6
        elif w in 'MNO':
            time += 7
        elif w in 'PQRS':
            time += 8
        elif w in 'TUV':
            time += 9
        elif w in 'WXYZ':
            time += 10
    print(time)