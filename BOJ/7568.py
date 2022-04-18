# 백준 [덩치]
# 브루트 포스
n = int(input())
arr = []

# n = 5
# arr = [[55, 185], [58, 183], [88, 186], [60, 175], [46, 155]]
answer = []

for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])

for i in range(n):
    k = 0
    a, b = arr[i][0], arr[i][1]
    for j in range(n):
        p, q = arr[j][0], arr[j][1]
        if a < p and b < q :
            k += 1
    answer.append(k + 1)

print(' '.join(map(str, answer)))