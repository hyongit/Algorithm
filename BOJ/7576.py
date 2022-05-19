# 백준 [토마토]
import sys
from collections import deque

input = sys.stdin.readline
m, n = map(int, input().split())

boxes = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            q.append([i, j])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()

        # 왼, 오, 앞, 뒤
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0:
                q.append([nx, ny])
                boxes[nx][ny] = boxes[x][y] + 1
bfs()
time = 0

for box in boxes:
    for i in box:
        if i == 0:
            print(-1)
            exit(0)
    time = max(time, max(box))

print(time-1)