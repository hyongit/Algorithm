from collections import deque

# BFS, 너비 우선 탐색, 큐 사용, 가까운 노드부터 탐색
# 1. 탐색 시작 노드를 큐에 삽입하고 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤에 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리
# 3. 더 이상 이 과정을 수행할 수 없을 때까지 반복

#BFS 메서드 정의
def bfs(graph, start, visited):
    # 시작 노드를 큐에 삽입
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        n = queue.popleft()
        print(n, end =' ')
        for i in graph[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

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

visited = [False] * 9

bfs(graph, 1, visited)
