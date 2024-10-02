import sys

if __name__ == '__main__':
    word = sys.stdin.readline().rstrip()
    dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    time = 0
    for w in word:
        for d in dial:
            if w in d:
                time += dial.index(d) + 3
    print(time)