# 백준 [치킨 거리]
# 시뮬레이션

from itertools import combinations

# n, m = map(int, input().split())
# maps = [list(map(int, input().split())) for _ in range(n)]

n, m = 5, 2
maps = [[0, 2, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 0, 0, 0], [2, 0, 0, 1, 1], [2, 2, 0, 1, 2]]

home_loca = []
chic_loca = []

answer = int(1e9)

for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            home_loca.append([i, j])
        if maps[i][j] == 2:
            chic_loca.append([i, j])

# print(home_loca)
# print(chic_loca)

for i in combinations(chic_loca, m):
    tmp = 0
    tmp_arr2 = []
    #print(i)
    for j in range(len(home_loca)):
        tmp_arr = []
        for k in range(len(i)):
            tmp = abs(home_loca[j][0] - i[k][0]) + abs(home_loca[j][1] - i[k][1])
            tmp_arr.append(tmp)
        tmp_arr2.append(min(tmp_arr))
    #print(sum(tmp_arr2))
    answer = min(answer, sum(tmp_arr2))

print(answer)