# 백준 [트리의 부모 찾기]
# DFS
import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n+1)]


visit = [0] * (n+1) # 방문 처리
answer = [0] * (n+1) # 정답 삽입할 리스트

visit[1] = 1 # 1이 루트이므로 방문 처리

for i in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# graph : [[], [6, 4], [4], [6, 5], [1, 2, 7], [3], [1, 3], [4]]

def dfs(d):
    for i in graph[d]:
        if visit[i] == 0:
            visit[i] = 1 # 방문 처리
            answer[i] = d # 정답 리스트에 i번째를 루트인 d로 변경
            dfs(i)

dfs(1) # 루트 노드부터 dfs 시작

# answer : [0, 0, 4, 6, 1, 3, 1, 4]
for j in range(2, n+1):
    print(answer[j])