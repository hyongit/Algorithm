# 백준 [바이러스]
# DFS

n = int(input())
m = int(input())
maps = [[] for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    maps[a].append(b)
    maps[b].append(a)

visited = [False] * (n+1)
answer = 0

def dfs(num):
    global answer

    visited[num] = True

    for i in range(len(maps[num])):
        if visited[maps[num][i]] == False:
            dfs(maps[num][i])
            answer += 1
            

dfs(1)
print(answer)
