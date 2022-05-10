# 백준 [단지 번호 붙이기]
# DFS, BFS
from collections import deque

n = int(input())
m = 2
arr = [input() for _ in range(n)]
maps = []

for i in arr:
    tmp = []
    for j in range(n):
        tmp.append(int(i[j]))
    maps.append(tmp)

# n = 7
# m = 2
# maps = [[0, 1, 1, 0, 1, 0, 0], [0, 1, 1, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 1], 
# [0, 0, 0, 0, 1, 1, 1], [0, 1, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 1, 0], 
# [0, 1, 1, 1, 0, 0, 0]]
answer = []

# 우, 좌, 하, 상
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1] 

def bfs(a, b):
    x, y = a, b
    cnt = 0

    maps[x][y] = m
    cnt += 1

    q = deque()
    q.append([x, y])

    while q :
        x, y = q.popleft()
        #print(x, y)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] == 1:
                # 큐에 push할 때 visit 체크 해줘야됨
                # pop할 때 할 때 하면 메모리 초과 !!
                maps[nx][ny] = m
                q.append([nx, ny])
                cnt+=1
    
    answer.append(cnt)
    return

def recur():
    global m
    for i in range(n):
        for j in range(n):
            if maps[i][j] == 1:
                bfs(i, j)
                m+=1

recur()
answer.sort()

print(m-2)
for i in answer:
    print(i)