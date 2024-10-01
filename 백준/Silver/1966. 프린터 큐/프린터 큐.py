from collections import deque

if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        N, M = map(int, input().split())
        deq = deque(list(map(int, input().split())))
        count = 0

        while deq:
            deq_max = max(deq)
            deq_front = deq.popleft()
            M -= 1

            if deq_front == deq_max:
                count += 1
                if M < 0:
                    print(count)
                    break
            else:
                deq.append(deq_front)
                if M < 0:
                    M = len(deq) - 1