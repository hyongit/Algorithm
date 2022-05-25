# 백준 [안전 영역]

from collections import deque
import sys

input = sys.stdin.readline
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

max_num = 0

safety_zone = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in maps:
    for j in i:
        if max_num < j:
            max_num = j


def bfs(a, b, graph):
    q = deque()
    x, y = a, b
    q.append([x, y])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and graph[nx][ny] != 0 and graph[nx][ny] != 101:
                graph[nx][ny] = 101
                q.append([nx, ny])


def rain(a):
    arr = [[0] * n for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(n):
            arr[i][j] = maps[i][j]
            if arr[i][j] <= a:
                arr[i][j] = 0

    for r in range(n):
        for c in range(n):
            if arr[r][c] != 0 and arr[r][c] != 101:
                bfs(r, c, arr)
                total += 1

    safety_zone.append(total)


for num in range(0, max_num+1):
    rain(num)

print(max(safety_zone))