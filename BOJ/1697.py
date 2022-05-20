# 백준 [연결 요소의 개수]

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visit = [0]*(n+1)
answer = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(num):

    visit[num] = 1
    
    for i in graph[num]:
        if visit[i] == 0:
            dfs(i)

for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        answer += 1

print(answer)