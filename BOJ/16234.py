# 백준 [인구이동]
# bfs, 시뮬레이션
import sys
import math
from collections import deque

input = sys.stdin.readline

# 남 동 북 서
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# n, l, r 입력
n, l, r = map(int, input().split())
# n*n의 땅 입력
maps = [list(map(int, input().split())) for _ in range(n)]

# n, l, r = 4, 10, 50
# maps = [[10, 100, 20, 90], [80, 100, 60, 70], [70, 20, 30, 40], [50, 20, 100, 10]]

# bfs 함수 정의
def bfs(i, j):
    # 큐 생성 후 현재 좌표 넣어주기
    q = deque()
    q.append((i, j))
    # 방문 처리
    visit[i][j] = True
    # 연합된 국가 담기
    union = [(i, j)]
    # 총 연합된 인구 수
    count = maps[i][j]
    # 인접 국가를 탐색하면서 인구 차이 l 이상 r 이하인 경우 연합 국가에 담기
    while q:
        x, y = q.popleft()
        # 4 방향 인접 국가 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 땅 범위 넘어가면
            if nx >= n or ny >= n or nx < 0 or ny < 0:
                continue
            # 방문 했으면
            if visit[nx][ny]:
                continue
            # 인구차이 l 이상, r 이하인 경우
            if l <= abs(maps[x][y] - maps[nx][ny]) <= r:
                # 연합 국가 배열에 좌표 담기
                union.append((nx, ny))
                # 방문 처리
                visit[nx][ny] = True
                # 큐에 좌표 넣기
                q.append((nx, ny))
                # count에 좌표의 인구 수 더해줌
                count += maps[nx][ny]
    # 연합 국가 간 인구 수는 (연합 인구수) / (연합 칸의 개수)
    for x, y in union:
        maps[x][y] = math.floor(count/len(union))
    
    return len(union)


answer = 0
# 인구 이동이 없을 때까지 무한 루프
while True:
    visit = [[False] * n for _ in range(n)]
    # 인구 이동 존재 유무 플래그
    flag = False
    # 모든 곳을 bfs로 방문하여 연합
    for i in range(n):
        for j in range(n):
            if not visit[i][j]:
                if bfs(i, j) > 1:
                    flag = True
    # 모든 곳 방문했는데도 인구 이동 없는 경우 break
    if not flag:
        break
    # 답 개수 늘리기
    answer += 1

print(answer)