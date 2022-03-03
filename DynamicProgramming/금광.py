# 다이나믹 프로그래밍
import sys
t = int(input())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().strip().split())
    arr = list(map(int, sys.stdin.readline().strip().split()))

    # dp 테이블 초기화
    dp = []
    idx = 0

    for _ in range(n):
        dp.append(arr[idx:idx+m])
        idx += m

    for j in range(1, m):
        for i in range(n):
            #왼쪽 위에서 오는 경우
            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            #왼쪽에서 오는 경우
            left = dp[i][j-1]

            #왼쪽 아래에서 오는 경우
            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            dp[i][j] = dp[i][j] + max(left_up, left, left_down)

    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)