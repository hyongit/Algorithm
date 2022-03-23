# 백준 [로봇 청소기]

n, m = map(int, input().split())

visited = [[0] * m for _ in range(n)] # 청소 여부


x, y, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited[x][y] = 1 #현재 위치 청소!!

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left(): #왼쪽 회전
    global d
    d -= 1 
    if d == -1:
        d = 3

count = 1 # 현재 위치를 청소 했음으로 1
turn_time = 0 # 회전 수 계산

while True:
    turn_left() # 왼쪽 방향 회전
    nx = x + dx[d]
    ny = y + dy[d]

    # 이동 시 방문하지 않았거나, 빈공간이면
    if visited[nx][ny] == 0 and arr[nx][ny] == 0:
        # 청소 여부 1로
        visited[nx][ny] = 1
        # 위치 이동
        x = nx
        y = ny
        # 카운트 늘림
        count += 1
        # 방향 초기화
        turn_time = 0
        continue

    # 이동 불가능 횟수 증가
    else:
        # 횟수 증가
        turn_time += 1

    if turn_time == 4: # 총 4번 회전 한 경우, 네 방향 모두 청소 되어 있거나 벽이 있으면
        # 일단 nx, ny 뒤로 이동시켜보기
        nx = x - dx[d]
        ny = y - dy[d]

        # 이동한 위치가 벽이 아님 -> 위치 이동
        if arr[nx][ny] != 1:
            x = nx
            y = ny

        # 벽임
        else:
            # 작동 멈춤
            break
        # 왼쪽 방향 회전 횟수 초기화
        turn_time = 0

# count 출력
print(count)