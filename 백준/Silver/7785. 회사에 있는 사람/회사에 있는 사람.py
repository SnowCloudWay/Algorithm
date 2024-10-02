import sys

if __name__ == '__main__':
    n = int(input())

    st = set()
    for _ in range(n):
        name, state = map(str, sys.stdin.readline().split())
        if state == "enter":
            st.add(name)
        elif state == "leave":
            st.discard(name)

    print('\n'.join(sorted(st, reverse=True)))