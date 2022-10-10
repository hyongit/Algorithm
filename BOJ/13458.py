# 백준 [시험 감독]
# while문 쓰면 시간초과, 사칙연산으로 풀기

n = int(input())
tmp_arr = map(int, input().split())
arr = []
for a in tmp_arr:
    arr.append(a)
b, c = map(int, input().split())

total = 0

for j in arr:
    j -= b
    total += 1

    if j > 0:
        if j % c == 0:
            total += j//c
        else:
            total += (j//c + 1)
    else:
        continue

print(total)