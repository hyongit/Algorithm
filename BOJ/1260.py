# 백준 [DFS와 BFS]

from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
dfs_visit = [0 for _ in range(n+1)]
bfs_visit = [0 for _ in range(n+1)]

for _ in range(m) :
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

for i in range(1, n+1):
    graph[i].sort()

def dfs(v):
    dfs_visit[v] = 1
    print(v, end=' ')

    for i in graph[v]:
        if dfs_visit[i] == 0:
            dfs(i)

def bfs(v):
    q = deque()
    q.append(v)
    bfs_visit[v] = 1
    
    while q:
        n = q.popleft()
        print(n, end=' ')
        for i in graph[n]:
            if bfs_visit[i] == 0:
                q.append(i)
                bfs_visit[i] = 1     

dfs(v)
print()
bfs(v)