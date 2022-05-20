# 백준 [연산자 끼워넣기]
# DFS(재귀), 브루트포스, 백트래킹
# 나누기 주의

n = int(input())
arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())

# n = 6
# nums = [1, 2, 3, 4, 5, 6]
# plus, minus, mul, div = 2, 1, 1, 1

max_num = int(-1e9)
min_num = int(1e9)

def recur(num, idx, plus, minus, mul, div):
    global max_num, min_num

    if idx == n-1:
        max_num = max(max_num, num)
        min_num = min(min_num, num)

    if plus > 0:
        recur(num + arr[idx+1], idx+1, plus-1, minus, mul, div)
    if minus > 0:
        recur(num - arr[idx+1], idx+1, plus, minus-1, mul, div)
    if mul > 0:
        recur(num * arr[idx+1], idx+1, plus, minus, mul-1, div)
    if div > 0:
        recur(int(num / arr[idx+1]), idx+1, plus, minus, mul, div-1)

recur(arr[0], 0, plus, minus, mul, div)

print(max_num)
print(min_num)