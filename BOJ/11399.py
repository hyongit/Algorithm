# 백준 [ATM]
# 그리디 알고리즘

n = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = []
ans.append(nums[0])

tmp = nums[0]

for i in range(1, n):
    tmp += nums[i]
    ans.append(tmp)

print(sum(ans))