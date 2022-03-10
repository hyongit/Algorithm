#다이나믹 프로그래밍, 가장 긴 증가하는 부분수열
import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
arr.reverse()

dp = [1] * n

# LIS 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(n - max(dp))