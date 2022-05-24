# 백준 [숨바꼭질]
from collections import deque

#n, k = map(int, input().split())

n, k = 5, 17
max_num = 100000
dist = [0]*(max_num+1)

def bfs():
    q = deque()
    q.append(n)

    while q:
        x = q.popleft()
        
        if x == k:
            print(dist[x])
            break
        
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_num and not dist[i]:
                # 높이 저장
                dist[i] = dist[x]+1
                print(dist[i], dist[x])
                q.append(i)
        
bfs()