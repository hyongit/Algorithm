# 백준 N과 M (5)

n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
arr = []

visit = [0] * n

def recur(num):

    if len(arr) == m :
        print(' '.join(map(str, arr)))
        return

    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            arr.append(nums[i])
            recur(num+1)
            visit[i] = 0
            arr.pop()

recur(0)