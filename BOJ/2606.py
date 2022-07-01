# 백준 [바이러스]
# DFS

n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

visited = [0] * (n+1)
ans = 0

visited[1] = 1

def dfs(num):
    for i in maps[num]:
        if visited[i] == 0:
            visited[i] = 1
            dfs(i)
            
dfs(1)

# [0, 1, 1, 1, 0, 1, 1, 0]
for i in range(2, n+1):
    if visited[i] == 1:
        ans += 1

print(ans)
