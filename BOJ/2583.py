# 백준 [영역 구하기]
from collections import deque

m, n, k = map(int, input().split())
graph = [[0] * n for _ in range(m)]

for _ in range(k):
    r_x, r_y, l_x, l_y = map(int, input().split())
    for i in range(r_y, l_y):
        for j in range(r_x, l_x):
            graph[i][j] = 1

# m, n, k = 5, 7, 3
# graph = [[0, 0, 0, 0, 1, 1, 0], [0, 1, 0, 0, 1, 1, 0], [1, 1, 1, 1, 0, 0, 0], 
#     [1, 1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0]]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

answer = []
d = 0

def dfs(a, b):
    global d

    q = deque()
    q.append([a, b])

    graph[a][b] = 2
    d += 1

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = 2
                d += 1
    return

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            dfs(i, j)
            answer.append(d)
            d = 0

answer.sort()
print(len(answer))
print(' '.join(map(str, answer)))