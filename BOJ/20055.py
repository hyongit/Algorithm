# 백준 [컨베이어 벨트 위의 로봇]
# 구현, 시뮬레이션, 덱
from collections import deque

n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))

# n, k = 3, 2
# arr = deque([1, 2, 1, 2, 1, 2])
robots = deque(list([0]*(2*n)))
level = 1

while True:
    # 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
    arr.rotate(1)
    robots.rotate(1)
    # 로봇이 내리는 위치에 도달하면 즉시 내림
    robots[n-1] = 0
    
    # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    for i in range(n-2, -1, -1):
        if robots[i] and not robots[i+1] and arr[i+1]:
            robots[i], robots[i+1] = 0, 1
            arr[i+1] -= 1

    # 로봇이 내리는 위치에 도달하면 즉시 내림
    robots[n-1] = 0

    # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올린다.
    if not robots[0] and arr[0]:
        robots[0] = 1
        arr[0] -= 1

    if arr.count(0) >= k:
        print(level)
        break
    level += 1

