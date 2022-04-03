# 백준 [스타트와 링크]
# 백트래킹, 조합 구현
# 백트래킹 - 재귀함수 -> 재귀함수 STACK으로 동작
import sys

input = sys.stdin.readline
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [False] * (n+1)
result = int(1e9)

def recur(num, idx):
    global result

    if num == (n//2):
        start, link = 0, 0
        for j in range(1, n+1):
            for k in range(1, n+1):
                if visited[j] and visited[k]:
                    start += arr[j-1][k-1]
                if not visited[j] and not visited[k]:
                    link += arr[j-1][k-1]

        result = min(result, abs(start-link))
        #return
        
    for i in range(idx, n+1):
        visited[i] = True
        recur(num+1, i+1)
        visited[i] = False

recur(0 , 1)
print(result)