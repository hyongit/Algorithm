# 백준 [퇴사]
#다이나믹 프로그래밍 : 큰 문제를 작은 문제로 나누어서 문제를 푸는 것
#뒤 쪽 날짜부터 거꾸로 확인하는 방식으로 접근
#현재 상담 일자의 이윤 + 현재 상담을 마친 일자부터의 최대 이윤

n = int(input())
t = []
p = []
dp = [0] * (n+1)
max_value = 0 #뒤부터 계산했을 때 현재까지의 최대 상담 금액

for _ in range(n):
    day, pay = list(map(int, input().split()))
    t.append(day)
    p.append(pay)

for i in range(n-1, -1, -1):
    time = t[i] + i

    if time <= n:
        dp[i] = max(p[i] + dp[t[i] + i], max_value)
        max_value = dp[i]
    else:
        dp[i] = max_value

print(max_value)