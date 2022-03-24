from itertools import combinations

n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

# n, m = 5, 1
# maps = [[1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0], [1, 2, 0, 0, 0]]

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
    tmp_arr = []
    for j in range(len(home_loca)):
        tmp = abs(home_loca[j][0] - i[0][0]) + abs(home_loca[j][1] - i[0][1])
        tmp_arr.append(tmp)
    answer = min(answer, sum(tmp_arr))

print(answer)