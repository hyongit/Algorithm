# 백준 [촌수계산]
# DFS

n = int(input())
a, b = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n+1)]
check = [0] * (n+1)

for i in range(m):
    j, k = map(int, input().split())
    graph[j].append(k)
    graph[k].append(j)

def dfs(d):
    for i in graph[d]:
        if check[i] == 0:
            check[i] = check[d]+1
            dfs(i)
             
dfs(a)

if check[b] > 0:
    print(check[b])
else:
    print(-1)