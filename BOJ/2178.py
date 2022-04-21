# 백준 [미로 탐색]
# BFS, 너비 우선 탐색

from collections import deque

n, m = map(int, input().split())
arr = [input() for _ in range(n)]
maps = []

for i in arr:
    tmp = []
    for j in range(m):
        tmp.append(int(i[j]))
    maps.append(tmp)

# n, m = 4, 6
# maps = [[1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 1, 0], [1, 0, 1, 0, 1, 1], [1, 1, 1, 0, 1, 1]]

answer = 0


# 우, 좌, 하, 상
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(a, b):
    global answer
    x, y = a, b

    q = deque()
    q.append([x, y])

    while q:
        x, y = q.popleft()
        #print(x, y)

        if x == n-1 and y == m-1:
            #print(maps)
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                if maps[nx][ny] == 1 :
                    maps[nx][ny] = maps[x][y] + 1
                    q.append([nx, ny])
    
    return maps[n-1][m-1]

print(dfs(0, 0))