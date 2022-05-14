# 백준 [RGB거리]
# 구현

n = int(input())
rgb = []

for _ in range(n):
    arr = list(map(int, input().split()))
    rgb.append(arr)

# n = 3
# rgb = [[1, 100, 100], [100, 1, 100], [100, 100, 1]]

for i in range(1, n):
    rgb[i][0] = min(rgb[i-1][1], rgb[i-1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i-1][0], rgb[i-1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i-1][0], rgb[i-1][1]) + rgb[i][2]

print(min(rgb[n-1]))