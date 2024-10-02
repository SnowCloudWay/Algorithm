n = int(input())
arr = []
for i in range(0,n):
    v = input()
    arr.append(v)
arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))
for i in arr:
    print(i)