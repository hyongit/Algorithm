# [백준] 2*n 타일링
# DP

n = int(input())
dp = [0] * 1000

dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = dp[i-2] + dp[i-1]

print(dp[n-1]%10007)