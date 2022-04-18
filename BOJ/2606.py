# 백준 [바이러스]
# DFS

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()
    
def dfs(num):
    global answer
    
    if visited[num] == 0:
        visited[num] = 1
        #print(num)

    for i in graph[num]:
        if visited[i] == 0:
            answer += 1
            dfs(i)
dfs(1)
print(answer)