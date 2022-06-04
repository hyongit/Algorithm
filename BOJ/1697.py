# 백준 [숨바꼭질]
from collections import deque

n, k = map(int, input().split())

#n, k = 5, 17

# 레벨을 저장할 리스트
point = [0] * (100000+1)

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x == k:
            print(point[k])
            break

		# [x-1, x+1, x*2]을 BFS 돌리면서 리스트에 i번째 수에 레벨을 저장함
        for i in [x-1, x+1, x*2]:
            # i가 나오는 가장 빠른 초만 저장하면됨
            # point[i]가 0이 아닌 숫자가 저장되어 있을 시 숫자 저장 X
            if 0 <= i <= 100000 and not point[i]:
                q.append(i)
								# 리스트의 i번째에 레벨 저장
                point[i] = point[x] + 1

bfs()