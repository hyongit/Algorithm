# 백준 [뱀]
# 시뮬레이션

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
    # 뱀의 머리 위치
    x, y = 1, 1
    # 뱀이 존재하는 위치는 2로 표시
    arr[x][y] = 2
    # 처음에는 direction 동쪽(0)
    d = 0
    # 시작한 뒤로부터 흐른 시간
    time = 0
    # 다음에 회전할 정보
    idx = 0
    # 뱀 (큐로 표현)
    q = [(x, y)]

    while True:
        # 이동한 위치 계산
        nx = x + dx[d]
        ny = y + dy[d]
        # 이동한 위치가 맵 범위 안에 있고, 뱀의 몸통이 없는 위치일 때
        if 1 <= nx <= n and 1 <= ny <= n and arr[nx][ny] != 2:
            # 사과가 없다면 이동 후 꼬리 제거
            if arr[nx][ny] == 0:
                # 뱀 머리 이동
                arr[nx][ny] = 2
                q.append((nx, ny))
                #꼬리 제거
                pastX, pastY = q.pop(0)
                arr[pastX][pastY] = 0
            #사과가 있다면 이동 후 꼬리 그대로
            if arr[nx][ny] == 1:
                arr[nx][ny] = 2
                q.append((nx, ny))
        #벽이나 몸통에 부딪혔다면
        else:
            time += 1
            break

        # 실행할 때마다 time 및 뱀 머리 이동
        x, y = nx, ny
        time += 1

        #회전할 시간의 경우
        if idx < l and time == info[idx][0]:
            d = turn(d, info[idx][1])
            idx += 1

    return time

n = int(input())
k = int(input())
# 맵 정보
arr = [[0] * (n+1) for _ in range(n+1)]
# 방향 전환 정보
info = []
# 처음에 동쪽을 보고 있으므로 (동 0, 남 1, 서 2, 북 3)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
# 사과가 있는 곳은 1로
for _ in range(k):
    i, j = map(int, input().split())
    arr[i][j] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

print(simulate())