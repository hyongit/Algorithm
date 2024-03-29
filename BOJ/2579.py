# [백준] 계단 오르기
# DP

n = int(input())
stairs = [0 for _ in range(301)]
dp = [0]*301

for k in range(n):
    stairs[k] = int(input())

dp[0] = stairs[0]
dp[1] = max(stairs[0]+stairs[1], stairs[1])
dp[2] = max(stairs[0]+stairs[2], stairs[1]+stairs[2])

for i in range(3, n):
    dp[i] = max(dp[i-2]+stairs[i], dp[i-3]+stairs[i-1]+stairs[i])

print(dp[n-1])