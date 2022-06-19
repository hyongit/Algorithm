# 백준 [로봇 청소기]
# 시뮬레이션, 구현

n, m = map(int, input().split())
r, c, d = map(int, input().split())

maps = []

for i in range(n):
    arr = list(map(int, input().split()))
    maps.append(arr)

# 북, 동, 남, 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

maps[r][c] = 2
ans = 1

x, y = r, c
cnt = 0

def turn(dir):
    return (dir-1) % 4

while True:
    d = turn(d)

    nx, ny = x + dx[d], y + dy[d]

    # 2a 왼쪽 청소하지 않은 빈 공간 존재 O
    if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 0:
        x, y = nx, ny
        maps[x][y] = 2
        ans += 1
        cnt = 0
        continue
    
    # 2a 왼쪽 청소하지 않은 빈 공간 존재 X
    else:
        cnt += 1

    # 후진하거나 종료
    if cnt == 4:
        nx, ny = x - dx[d], y - dy[d]

        if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] != 1:
            x, y = nx, ny
        else:
            break 
        
        cnt = 0

print(ans)