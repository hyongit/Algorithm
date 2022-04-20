# 백준 N과 M (2)

n, m = map(int, input().split())
arr = []

def recur(num):
    if len(arr) == m :
        print(' '.join(map(str, arr)))
        return

    for i in range(num, n+1):
        arr.append(i)
        recur(i+1)
        arr.pop()

recur(1)