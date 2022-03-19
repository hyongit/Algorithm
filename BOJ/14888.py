n = int(input())
nums = list(map(int, input().split()))
plus, minus, mul, div = list(map(int, input().split()))

min_ans, max_ans = 1e9, -1e9

def dfs(num, idx, plus, minus, mul, div):
    global max_ans, min_ans

    if idx == n:
        max_ans = max(max_ans, num)
        min_ans = min(min_ans, num)

    if plus > 0:
        dfs(num + nums[idx], idx + 1, plus-1, minus, mul, div)
    if minus > 0:
        dfs(num - nums[idx], idx + 1, plus, minus-1, mul, div)
    if mul > 0:
        dfs(num * nums[idx], idx + 1, plus, minus, mul-1, div)
    if div > 0:
        dfs(int(num / nums[idx]), idx + 1, plus, minus, mul, div-1)


dfs(nums[0], 1, plus, minus, mul, div)
print(max_ans)
print(min_ans)