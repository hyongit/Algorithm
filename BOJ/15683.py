# [백준] 감시

import copy


n, m = 6, 6
maps = [[0, 0, 0, 0, 0, 0], [0, 2, 0, 0, 0, 0], [0, 0, 0, 0, 6, 0], [0, 6, 0, 0, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 5]]
# n, m = map(int, input().split())
# maps = []
# for _ in range(n):
#     tmp_map = list(map(int, input().split()))
#     maps.append(tmp_map)

#     상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# cctv 종류에 따른 감시 방향
direction = {
    1 : [[0], [1], [2], [3]],
    2 : [[0, 2], [1, 3]],
    3 : [[0, 1], [1, 2], [2, 3], [3, 0]],
    4 : [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
    5 : [[0, 1, 2, 3]]
}

cctv = [] # cctv 리스트
ans = int(1e9) # 사각지대 크기

# cctv 찾기
for i in range(n):
    for j in range(m):
        if maps[i][j] != 0 and maps[i][j] != 6:
            cctv.append([i, j, maps[i][j]]) # x좌표, y좌표, cctv 종류

# print(cctv)

def watch(x, y, direction, tmp):
    for d in direction:
        nx, ny = x, y
        #print(nx, ny)
        # 이동할 수 없을 때까지 이동하면서 '#'으로 변경
        while True:
            nx += dx[d]
            ny += dy[d]

            if nx < 0 or nx >= n or ny < 0 or ny >= m or tmp[nx][ny] == 6:
                break
            elif tmp[nx][ny] == 0: # 빈 칸이면 감시구역으로 변경
                tmp[nx][ny] = '#'
    
    #print(tmp)

def dfs(n, maps):
    global ans
    
    tmp = copy.deepcopy(maps)
    #print(n, tmp)

    if n == len(cctv):
        cnt = 0 # 빈 칸 개수
        for t in tmp:
            cnt += t.count(0)
        ans = min(ans, cnt)
        return
    
    x, y, c = cctv[n]

    # 해당 cctv 종류에 따른 감시 구역을 구한다
    for d in direction[c]:
        #print(d)
        watch(x, y, d, tmp)
        dfs(n+1, tmp)
        tmp = copy.deepcopy(maps)

dfs(0, maps)
print(ans)