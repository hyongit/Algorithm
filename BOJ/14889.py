# 백준 [스타트와 링크]
# DFS로 조합 구현
# DFS는 재귀함수 -> 재귀함수 STACK으로 동작

import sys
input = sys.stdin.readline

def dfs(dep, idx):
    global min_num

    if dep == (n//2) :
        start, link = 0, 0
        for j in range(n):
            for k in range(n):
                if visited[j] and visited[k]:
                    start += graph[j][k]
                elif not visited[j] and not visited[k]:
                    link += graph[j][k]

        min_num = min(min_num, abs(start - link))

    for i in range(idx, n):
        visited[i] = True
        dfs(dep+1, i+1)
        visited[i] = False


n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * n
min_num = int(1e9)
dfs(0, 0)

print(min_num)