n = int(input())
arr = list(map(int, input().split()))

d = [0] * n
d[0] = arr[0]
d[1] = arr[1]

for i in range(2, n):
    tmp = 0
    d[i] = max(d[i-1], d[i-2]+arr[i])

print(d) # 1 3 3 8
print(max(d)) # 8