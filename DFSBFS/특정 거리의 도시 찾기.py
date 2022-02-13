import sys
from collections import deque
# 최단 거리 -> BFS

n, m, k, x = map(int,input().split())
graph = [[] for _ in range(n+1)]
answer = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화
distance = [0] * (n+1)
visited = [False] * (n+1)
#출발 도시까지의 거리는 0으로 설정
distance[x] = 0

#너비 우선 탐색 수행
q = deque([x])
visited[x] = True

while q:
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    now = q.popleft()
    for i in graph[now]:
        #아직 방문하지 않은 도시라면
        if visited[i] == False:
            visited[i] = True
            q.append(i)
            #최단 거리 갱신
            distance[i] += distance[now] + 1
            if distance[i] == k:
                answer.append(i)

answer.sort()

if len(answer) == 0:
    print(-1)
else:
    for i in answer:
        print(i)