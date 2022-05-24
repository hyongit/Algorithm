# 백준 [미로 탐색]
from collections import deque

n, m = map(int, input().split())
maps = []
arr = []

for _ in range(n):
    nums = input()
    arr.append(nums)

for i in arr:
    tmp = []
    for j in i:
        tmp.append(int(j))
    maps.append(tmp)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs():
    x, y = 0, 0
    q = deque()
    q.append([x, y])

    while q:    
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 전에 저장된 숫자 + 1 !!
                maps[nx][ny] = maps[x][y]+1
                q.append([nx, ny])

    # for i in maps:
    #     print(i)
    return maps[n-1][m-1]

print(dfs())