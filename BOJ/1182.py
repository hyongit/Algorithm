# 백준 [부분수열의 합]
# 백트래킹

n, s = map(int, input().split())
nums = list(map(int, input().split()))
# n, s = 5, 0
# nums = [-7, -3, -2, 5, 8]
total = 0

def dfs(idx, sum):
    global total

    if idx == n:
        return
    
    # (sum + 이번 숫자)가 s면
    if sum + nums[idx] == s : 
        total += 1
    
    dfs(idx+1, sum + nums[idx]) # 이번 숫자 포함
    dfs(idx+1, sum) # 이번 숫자 불포함

dfs(0, 0)
print(total)