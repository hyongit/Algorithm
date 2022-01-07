########### [이코테] 상하좌우 ##########
n = int(input())
li = list(input().split())
x, y = 1, 1
for i in li:
    if i == 'L':
        x, y = x, y-1
        if y == 0:
            y += 1

    elif i == 'R':
        x, y = x, y+1
        if y >= n:
            y -= 1

    elif i == 'U':
        x, y = x-1, y
        if x == 0:
            x += 1

    elif i == 'D':
        x, y = x+1, y
        if x >= n:
            x -= 1

print(x, y)
