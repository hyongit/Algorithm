# 다이나믹 프로그래밍
import sys

n, m = map(int, input().split())
arr = []

for _ in range(n):
    tmp = int(sys.stdin.readline())
    arr.append(tmp)

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j - arr[i]] != 10001 :
            d[j] = min(d[j], d[j - arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

