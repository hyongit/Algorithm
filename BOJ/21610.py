# 백준 [마법사 상어와 비바라기]
# 구현, 큐
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# n, m = 5, 4
# board = [[0, 0, 1, 0, 2], [2, 3, 2, 1, 0], [4, 3, 2, 9, 0], [1, 0, 2, 9, 0], [8, 8, 2, 1, 0]]

# 8개 방향 좌표
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

q = deque()
# 큐에 cloud의 초기 좌표값 삽입
q.append([n-2, 0])
q.append([n-2, 1])
q.append([n-1, 0])
q.append([n-1, 1])

for _ in range(m):
    # d, s 입력 받기
    d, s = map(int, input().split())
    # d, s = 1, 3
    # 구름 좌표 받을 2차원 배열
    cloud = [[0] * n for _ in range(n)]

    # q에서 원소 하나씩 꺼내서 옮기기 
    while q:
        x, y = q.popleft()
        nx = (x + dx[(d-1)]*s) % n 
        ny = (y + dy[(d-1)]*s) % n
        cloud[nx][ny] = 1
    
    # 구름 위치에 비 1씩
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1:
                board[i][j] += 1

    # 대각선 확인
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 1 :
                x, y = i, j
                cnt = 0
                for k in [1, 3, 5, 7] :
                    nx = x + dx[k]
                    ny = y + dy[k]
                    if nx < 0 or nx >= n or ny < 0 or ny >= n:
                        continue
                    else:
                        if board[nx][ny] > 0:
                            cnt+=1
                board[i][j] += cnt

    # 구름이 있었던 칸을 제외한 나머지 칸 중 물의 양이 2 이상인 칸에 구름 생성 (큐에 삽입)
    for i in range(n):
        for j in range(n):
            if cloud[i][j] == 0 and board[i][j] >= 2:
                board[i][j] -= 2
                q.append([i, j])

answer = 0

# board 값 다 더해서 결과
for i in range(n):
    for j in range(n):
        answer += board[i][j]

print(answer)

