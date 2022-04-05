# 백준 [로봇 청소기]
# 시뮬레이션, 구현

n, m = map(int, input().split())
r, c, d = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# n, m = 6, 6
# r, c, d = 2, 1, 3
# maps = [[1, 1, 1, 1, 1, 1], [1, 0, 0, 0, 0, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]

# 방향 북, 동, 남, 서
x, y = r, c
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 여부 = 2
#현재 위치 청소!!
maps[r][c] = 2
count = 1

#왼쪽 회전 함수
def rotate(num):
    result = (num - 1) % 4
    return result

# 회전 수 계산
flag = 0

while True:
    # 왼쪽 방향 회전
    d = rotate(d)

    nx = x + dx[d]
    ny = y + dy[d]

    # 이동 시 방문하지 않았거나, 빈공간이면
    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0 :
        # 청소 여부 2로
        maps[nx][ny] = 2
        
        # 위치 이동
        x, y = nx, ny
        # 카운트 늘림
        count += 1
        # 방향 초기화
        flag = 0
        continue

    # 이동 불가능 횟수 증가
    else :
        # 이동 횟수 증가
        flag += 1

    # 총 4번 회전 한 경우, 네 방향 모두 청소 되어 있거나 벽이 있으면
    if flag == 4 :
        # 일단 nx, ny 뒤로 이동시켜보기
        nx = x - dx[d]
        ny = y - dy[d]

        # 이동한 위치가 벽이 아님 -> 위치 이동
        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 1:
            x, y = nx, ny
        # 벽임
        else:
            # 작동 멈춤
            break
        
        # 왼쪽 방향 회전 횟수 초기화
        flag = 0

# count 출력
print(count)