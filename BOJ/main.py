n = 3
graph = [[0, 6, 7], [6, 0, 3], [7, 3, 0]]
visit = [0]*n
total = 0
min_total = int(1e9)

def dfs(idx, d):
    global min_total, total, visit

    visit[idx] = 1

    if d == 2:
        print(total)
        if min_total > total:
            min_total = total
        total = 0
        return

    for i in range(n):
        if visit[i] == 0 and i != idx:
            total += graph[idx][i]
            dfs(i, d+1)
            visit[i] = 0
        
dfs(0, 0)
print(min_total)