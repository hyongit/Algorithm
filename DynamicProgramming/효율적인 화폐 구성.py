# 다이나믹 프로그래밍
import sys

n, m = map(int, input().split())
arr = []

for i in range(n):
    tmp = int(sys.stdin.readline().strip())
    arr.append(tmp)

d = [10001] * (m+1)
d[0] = 0

for i in range(n):
    for j in range(arr[i], m+1):
        if d[j - arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])

# Ai = 금액 i를 만들 수 있는 최소한의 화폐 개수
# k = 각 화폐의 단위
# 점화식 :
# Ai-k를 만드는 방법이 존재하는 경우 (Ai-k가 10001이 아닌 경우), Ai = min(Ai, Ai-k+1)
# Ai-k를 만드는 방법이 존재하는 경우 (Ai-k가 10001), Ai = 10001
# Ai-k 만들 수 있으면 k원 만큼 추가하여 Ai를 만들 수 있음을 이용!