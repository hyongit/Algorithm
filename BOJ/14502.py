# 백준 [연구소]
# BFS
from collections import deque
import sys

input = sys.stdin.readline
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
#print(maps)

# n, m = 4, 6
# maps = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]

result = 0

#    왼, 오, 위, 아래
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

# bfs 함수
def bfs():
    global result
    total = 0

    # 배열 카피
    copymap = [[0]*m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            copymap[i][j] = maps[i][j]
    
    # 바이러스 (2가 있는) 위치 저장
    q = deque()
    for i in range(n):
        for j in range(m):
            if copymap[i][j] == 2:
                q.append([i, j])

    # 저장된 위치의 왼, 오, 위, 아래 검사
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and copymap[nx][ny] == 0:
                # 0인 값을 찾아 2로 바꿔주고 바꾼 곳의 위치 저장
                copymap[nx][ny] = 2
                q.append([nx, ny])

    # 안전구역 , (0의 개수) 세고 큰 값 저장
    for i in range(n):
        for j in range(m):
            if copymap[i][j] == 0:
                total += 1

    result = max(total, result)

# 벽 세우는 함수
def wall(num):
    # 벽 3개면 bfs 실행
    if num == 3:
        bfs()
        # 원래 자리로 돌아 가서 다시 또 다음 경우
        return

    # 0 이면 재귀적으로 벽 세워서 벽 세우는 모든 경우의 수 고려
    for i in range(n):
        for j in range(m):
           if maps[i][j] == 0:
               maps[i][j] = 1
               wall(num+1)
               maps[i][j] = 0
wall(0)
print(result)