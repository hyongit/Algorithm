# [백준] 모든 순열
# 백트래킹

n = int(input())
#n = 3
ans = []

def recur(num):
    if len(ans) == n:
        print(' '.join(map(str, ans)))
        return

    for i in range(num, n+1):
        if i not in ans:
            ans.append(i)
            recur(num)
            ans.pop()

recur(1)