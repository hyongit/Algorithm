import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    maps = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        maps[y][x] = 1

# t = 1
# m, n, k = 5, 3, 6
# maps = [[0, 0, 0, 0, 1], [0, 0, 0, 0, 0], [1, 1, 1, 1, 1]]

    #print(maps)

    # 하, 상, 우, 좌
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    answer = 0

    def bfs(a, b):
        q = deque()
        q.append([a, b])

        while q:
            x, y = q.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                    #print(nx, ny)
                    q.append([nx, ny])
                    maps[nx][ny] = 2
                    

    for i in range(n): # 3
        for j in range(m): # 5
            if maps[i][j] == 1 :            
                bfs(i, j)
                answer += 1

    print(answer)