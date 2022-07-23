# [백준] N과 M (6)

n, m = map(int, input().split())
nums = list(map(int, input().split()))

# n, m = 4, 2
# nums = [9, 8, 7, 1]

nums.sort()

ans = []

def recur(d):
    if len(ans) == m:
        print(' '.join(map(str, ans)))
        return
    
    for i in range(d, n):
        ans.append(nums[i])
        recur(i+1)
        ans.pop()

recur(0)
