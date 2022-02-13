# DFS, 깊이 우선 탐색, 스택, 재귀 사용
# 1. 탐색 시작 노드를 스택에 삽입하고 방문 처리 함
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접 노드를 스택에 넣고 방문 처리
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
# 3. 이 과정을 더 이상 수행할 수 없을 때까지 반복!

# DFS 메서드 정의
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for i in graph[v]:
        if visited[i] == False:
            dfs(graph, i, visited)

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보를 표현
visited = [False] * 9
#정의된 DFS 함수 호출
dfs(graph,1,visited)