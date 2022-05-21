# 백준 [스타트와 링크]
# 백트래킹, 조합 구현
# 백트래킹 - 재귀함수 -> 재귀함수 STACK으로 동작

n = int(input())
graph = []

# n = 6
# graph = [[0,1,2,3,4,5], [1,0,2,3,4,5], [1,2,0,3,4,5], [1,2,3,0,4,5], [1,2,3,4,0,5], [1,2,3,4,5,0]]
visit = [0] * (n+1)
result = int(1e9)

for i in range(n):
    tmp = list(map(int, input().split()))
    graph.append(tmp)

def recur(depth, idx):
    global result
    
    if depth == n//2:
        #print(visit)
        start, link = 0, 0
        tmp = 0

        for i in range(1, n+1):
            for j in range(1, n+1):
                if visit[i] and visit[j]:
                    start+=graph[i-1][j-1]
                if not visit[i] and not visit[j]:
                    link+=graph[i-1][j-1]
        
        if start>link:
            tmp = start-link
        else:
            tmp = link-start

        result = min(result, tmp)

        return
    
    for i in range(idx, n+1):
        visit[i] = 1
        recur(depth+1, i+1)
        visit[i] = 0

recur(0, 1)

print(result)