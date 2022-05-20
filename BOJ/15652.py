# 백준 [ N과 M (4) ]
# 백트래킹

#n, m = map(int, input().split())
n, m = 4, 2
arr =[]

def recur(num):

    if len(arr) == m:
        print(' '.join(map(str, arr)))
        return
    
    for i in range(num, n+1):
        arr.append(i)
        recur(i)
        arr.pop()

recur(1)