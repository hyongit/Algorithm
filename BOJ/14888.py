# 백준 [연산자 끼워넣기]
# DFS(재귀), 브루트포스, 백트래킹
# 나누기 주의

n = int(input())
nums = list(map(int, input().split()))

plus, minus, mult, div = map(int, input().split())

max_num = int(-1e9)
min_num = int(1e9)

def recur(plus, minus, mult, div, num, idx):
    global max_num, min_num

    if idx == len(nums)-1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)

    if plus > 0:
        recur(plus-1, minus, mult, div, num + nums[idx+1], idx+1)
    
    if minus > 0:
        recur(plus, minus-1, mult, div, num - nums[idx+1], idx+1)

    if mult > 0:
        recur(plus, minus, mult-1, div, num * nums[idx+1], idx+1)
    
    if div > 0:
        recur(plus, minus, mult, div-1, int(num / nums[idx+1]), idx+1)

recur(plus, minus, mult, div, nums[0], 0)
print(max_num)
print(min_num)