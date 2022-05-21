# 백준 [치즈]

from collections import deque

n, m = map(int, input().split())
graph = []

for i in range(n):
    arr = list(map(int, input().split()))
    graph.append(arr)

# n, m = 13, 12
# graph = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
#         [0, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0], 
#         [0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0], 
#         [0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0], 
#         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#         [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0], 
#         [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
ans = []


def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    cnt = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == 0:
                if graph[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx, ny])
                
                # 1에서 0이 된 곳만 0으로 바꾸기
                elif graph[nx][ny] == 1:
                    visited[nx][ny] = 1
                    graph[nx][ny] = 0
                    cnt+=1
    
    # for i in range(n):
    #     print(visited[i])
    # print()
    # for i in range(n):
    #     print(graph[i])
    # print()
    ans.append(cnt)
    return cnt

time = 0

while 1:
    time += 1
    visited = [[0]*m for _ in range(n)]
    cnt = bfs()
    
    if cnt == 0:
        break

print(time-1)
print(ans[-2])