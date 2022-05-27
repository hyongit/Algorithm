# 백준 [연결 요소의 개수]
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    # 두 리스트에 모두 append
    graph[a].append(b)
    graph[b].append(a)

visit = [0] * (n+1)
result = 0

def dfs(d):
    visit[d] = 1

    for j in graph[d]:
        if visit[j] == 0:
            dfs(j)
    return

for i in range(1, n+1):
    if visit[i] == 0:
        dfs(i)
        result+=1

print(result)
