n = int(input())
arr = list(map(int, input().split()))
rock = arr[0]
cnt = 1

for i in range(1, n):
    if arr[i] > rock:
        cnt += 1
        rock = arr[i]

print(cnt)
