# 백준 [뱀]
# 시뮬레이션
import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
k = int(input())

# 맵 정보
maps = [[0]*n for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    maps[a-1][b-1] = 1

# 방향 전환 정보
l = int(input())
times = []
for _ in range(l):
    x, c = input().split()
    times.append([int(x), c])

# 처음에 동쪽을 보고 있으므로 (동 0, 남 1, 서 2, 북 3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(d, c):
    # 동, 남, 서, 북 (0, 1, 2, 3)
    # 왼쪽으로 90도 회전 0 -> 3 -> 2 -> 1
    if c == 'L':
        d = (d - 1) % 4
    # 오른쪽으로 90도 회전 0 -> 1 -> 2 -> 3
    else:
        d = (d + 1) % 4
    
    return d

def simulate():
    # 초기 뱀의 위치
    x, y = 0, 0
    # 뱀이 존재하는 위치는 2로 표시
    maps[x][y] = 2
    # 처음에는 direction 동쪽(0)
    direction = 0
    # 시작한 뒤로부터 흐른 시간
    time = 0
    idx = 0
    # 뱀 (큐로 표현)
    q = deque([(x, y)])

    while True:
        # 이동한 위치 계산
        nx = x + dx[direction]
        ny = y + dy[direction]
        # 이동한 위치가 맵 범위 안에 있고, 뱀의 몸통이 없는 위치일 때
        if 0 <= nx < n and 0 <= ny < n and maps[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if maps[nx][ny] != 1:
                # 뱀 머리 이동
                maps[nx][ny] = 2
                q.append([nx, ny])
                #꼬리 제거
                temp_x, temp_y = q.popleft()
                maps[temp_x][temp_y] = 0

            #사과가 있다면 이동 후 꼬리 그대로
            if maps[nx][ny] == 1 :
                maps[nx][ny] = 2
                q.append([nx, ny])

        #벽이나 몸통에 부딪혔다면
        else :
            time += 1
            break

        # 실행할 때마다 time 및 뱀 머리 이동
        x, y = nx, ny
        #print(x, y)
        time += 1

        #회전할 시간의 경우
        if idx < l and  time == times[idx][0]:
            direction = turn(direction, times[idx][1])
            idx += 1
    
    return time

print(simulate())