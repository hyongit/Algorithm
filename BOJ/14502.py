# 백준 [연구소]
# BFS
# 재귀로 벽 세우는 모든 경우의 수 파악
# bfs로 바이러스 퍼뜨린 후 안전구역 세고 최댓값 저장

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# n, m = 4, 6
# arr = [[0, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 2], [1, 1, 1, 0, 0, 2], [0, 0, 0, 0, 0, 2]]

#    왼, 오, 위, 아래
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

answer = 0

def bfs():
    global answer
    # 배열 카피
    copy = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            copy[i][j] = arr[i][j]
    result = 0
    q = deque()

    # 바이러스 (2가 있는) 위치 저장
    for i in range(n):
        for j in range(m):
            if copy[i][j] == 2:
                q.append([i, j])
    # 저장된 위치의 왼, 오, 위, 아래 검사
    while q:
        x, y = q[0][0], q[0][1]
        q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m :
                # 0인 값을 찾아 2로 바꿔주고 바꾼 곳의 위치 저장
                if copy[nx][ny] == 0:
                    copy[nx][ny] = 2
                    q.append([nx, ny])
    # 안전구역 , (0의 개수) 세고 큰 값 저장
    for i in copy:
        for j in i:
            if j == 0:
                result += 1
    answer = max(result, answer)
    
# 벽 세우는 함수
def wall(cnt):
    # 벽 3개면 dfs 실행
    if cnt == 3:
        bfs()
        # 원래 자리로 돌아 가서 다시 또 다음 경우
        return

    # 0 이면 재귀적으로 벽 세워서 벽 세우는 모든 경우의 수 고려
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 0: 
                arr[i][j] = 1
                wall(cnt + 1)
                arr[i][j] = 0     

wall(0)
print(answer)