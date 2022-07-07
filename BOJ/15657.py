# [백준] N과 M (8)
# 백트래킹

n, m = map(int, input().split())
nums = list(map(int, input().split()))

nums.sort()
ans = []

def recur(d):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return

    for i in range(d, n):
        ans.append(nums[i])
        recur(i)
        ans.pop()

recur(0)