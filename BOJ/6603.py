# 백준 [로또]
# 백트래킹

import sys

input = sys.stdin.readline

def recur(d, idx):
    
    if d == 6:
        for i in range(6):
            print(result[i], end=' ')
        print()
        return

    for i in range(idx, n):
        if nums[i] not in result:
            result.append(nums[i])
            recur(d+1, i+1)
            result.pop()

# result = []
# n = 8
# nums = [1,2,3,5,8,13,21,34]
# recur(0, 0)

while True:

    nums = list(map(int, input().split()))
    n = nums[0]
    nums = nums[1:]

    if n == 0:
        break

    result = []
    recur(0, 0)
    print()