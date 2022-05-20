import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0, -1, -1, 1, 1]
dy = [0, 0, -1, 1, -1, 1, -1, 1]


def recur(arr, n, m):
    answer = 0

    for i in range(m): # 2
        for j in range(n): # 3
            if arr[i][j] == 1:
                dfs(arr, i, j, n, m)
                answer += 1

    return answer

def dfs(graph, a, b, c, d):
    x, y = a, b
    q = deque()
    q.append([x, y])
    graph[x][y] = 2

    while q:
        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < d and 0 <= ny < c and graph[nx][ny] == 1:
                graph[nx][ny] = 2
                q.append([nx, ny])

while True:
    w, h = map(int, input().split())

    if w == 0  and h == 0 :
        break

    maps = []
    
    for i in range(h):
        tmp = list(map(int, input().split()))
        maps.append(tmp)
    
    print(recur(maps, w, h))


# w, h = 5, 4

# maps = [[1,0,1,0,0], [1,0,0,0,0], [1,0,1,0,1], [1,0,0,1,0]]

# for i in range(h):
#     tmp = list(map(int, input().split()))
#     maps.append(tmp)

