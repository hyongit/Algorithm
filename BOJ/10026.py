# 백준 [적록색약]
# BFS는 큐에 넣을 때 방문 처리를 해야 메모리 초과가 안남!!!!!

from collections import deque

n = int(input())
tmp = [input() for _ in range(n)]

colors = []

visit = [[0] * n for _ in range(n)]

total = 0
rtotal = 0

for i in tmp:
    arr = []
    for j in i:
        arr.append(j)
    colors.append(arr)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(a, b, k):
    x, y = a, b
    q = deque()
    q.append([x, y])

    while q :
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if k == 'X':
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0 and colors[x][y] == colors[nx][ny]:
                    visit[nx][ny] = 1
                    q.append([nx, ny])

            else:
                if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                    if colors[x][y] == 'B':
                        if colors[x][y] == colors[nx][ny]:
                            visit[nx][ny] = 1
                            q.append([nx, ny])
                    else:
                        if colors[nx][ny] == 'R' or colors[nx][ny] == 'G':
                            visit[nx][ny] = 1
                            q.append([nx, ny])
                            

    return

# 적록색약 아닌 사람
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j, 'X')
            total += 1

visit = [[0] * n for _ in range(n)]

# 적록색약인 사람
for i in range(n):
    for j in range(n):
        if visit[i][j] == 0:
            visit[i][j] = 1
            bfs(i, j, 'O')
            rtotal += 1

print(total, rtotal)
