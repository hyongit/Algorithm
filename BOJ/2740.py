# [백준] 행렬 곱셈

n, m = map(int, input().split())
arr1 = [list(map(int, input().split())) for _ in range(n)]

m, k = map(int, input().split())
arr2 = [list(map(int, input().split())) for _ in range(m)]

answer = [[0]*k for _ in range(n)]

for row in range(n):
    for col in range(k):
        e = 0
        for i in range(m):
            e += arr1[row][i]*arr2[i][col]
        answer[row][col] = e

for i in answer:
    print(*i)
