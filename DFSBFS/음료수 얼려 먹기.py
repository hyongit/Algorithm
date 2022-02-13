# DFS, 하나의 노드에 연결된 노드 확인을 반복 --> 깊이 우선!
# 섬의 개수 찾는 문제와 비슷한 유형
import sys

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))

def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False # graph[x][y]가 원래 1인 경우

answer = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            answer += 1
print(answer)
