# 백준 [치킨 거리]
# 시뮬레이션

from itertools import combinations
from xml.dom import minicompat

# n, m = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(n)]

n, m = 5, 2
maps = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]

# 집 위치, 치킨 집 위치 저장
home_loca = []
chic_loca = []

min_loca = int(1e9)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1 :
            home_loca.append([i+1, j+1])
        elif maps[i][j] == 2 :
            chic_loca.append([i+1, j+1])

for i in combinations(chic_loca, m):
    tmp = 0
    result_loca = []

    for j in range(len(home_loca)):
        a, b = home_loca[j][0], home_loca[j][1]
        tmp_loca = []
        for k in range(len(i)):
            r, c = i[k][0], i[k][1]
            tmp = abs(a - r) + abs(b - c)
            tmp_loca.append(tmp)
        result_loca.append(min(tmp_loca))
    min_loca = min(min_loca, sum(result_loca))

print(min_loca)