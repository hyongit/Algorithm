T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    arr = [[0] * n for _ in range(n)]

    # 우, 하, 좌, 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    num, d = 1, 0
    x, y = 0, 0

    while num <= n**2:
        arr[x][y] = num
        num += 1

        # 범위 확인
        nx = x + dx[d]
        ny = y + dy[d]

        if nx < 0 or ny < 0 or nx >= n or ny >= n or arr[nx][ny] :
            d = (d+1) % 4

        # 숫자 변경
        x += dx[d]
        y += dy[d]

    for i in arr:
        print(' '.join(map(str, i)))