# 백준 [스위치 켜고 끄기]
from collections import deque

n = int(input())
state = list(map(int, input().split()))
m = int(input())
arr = []

for _ in range(m):
    a, b = map(int, input().split())
    arr.append([a, b])

lq = deque()
rq = deque()

for i in range(m):
    # 남학생
    if arr[i][0] == 1:
        for j in range(n):
            if (j+1) % arr[i][1] == 0:
                if state[j] == 0:
                    state[j] = 1
                else:
                    state[j] = 0

    #여학생
    if arr[i][0] == 2:
        num = arr[i][1]-1
        lq.append(num)
        rq.append(num)

        while lq:
            x = lq.popleft()
            y = rq.popleft()

            left = x-1 
            right = y+1

            if 0 <= left < n and 0 <= right < n and state[left] == state[right]:                
                if state[left] == 0:
                    state[left] = 1
                else:
                    state[left] = 0
                
                if state[right] == 0:
                    state[right] = 1
                else:
                    state[right] = 0

                lq.append(left)
                rq.append(right)
            
            else:
                if state[num] == 0:
                    state[num] = 1
                else:
                    state[num] = 0


for i in range(1, n+1):
    print(state[i-1], end=' ')

    if i % 20 == 0:
        print()
    