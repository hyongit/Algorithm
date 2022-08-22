# [백준] 돌려막기

a = [list(map(int, input().split())) for _ in range(5)]
b = [list(map(int, input().split())) for _ in range(5)]

tmp_1, tmp_2 = 0, 0
tmp_list = []

names = ['Inseo', 'Junsuk', 'Jungwoo', 'Jinwoo', 'Youngki']
names_reverse = ['Youngki', 'Jinwoo', 'Jungwoo', 'Junsuk', 'Inseo']

for x in range(5):
    for y in range(5):
        for i in range(5):
            tmp_1 += a[x][i] * b[i][y]
    tmp_list.append(tmp_1)
    tmp_1 = 0

if tmp_list.count(min(tmp_list)) > 1:
    tmp_list.reverse()
    print(names_reverse[tmp_list.index(min(tmp_list))])

else:
    print(names[tmp_list.index(min(tmp_list))])