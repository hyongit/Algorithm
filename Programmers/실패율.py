stages = [2, 1, 2, 6, 2, 4, 3, 3]
N = 5

stages.sort()
tmp = []
new_tmp = []
answer = []

for i in range(1, N + 1):
    n = 0
    for j in stages:
        if j <= i:
            n += 1
    if n == 0:
        tmp.append(0)
    else:
        tmp.append(n / len(stages))
    stages = stages[n:]

new_tmp = sorted(tmp)[::-1]

for j in range(len(new_tmp)):
    answer.append(tmp.index(new_tmp[j]) + 1)
    # 원소를 2로 바꿔줌으로써 중복 방지 !, 인덱스 적은 순으로 바꿔줌
    tmp[tmp.index(new_tmp[j])] = 2

print(answer)