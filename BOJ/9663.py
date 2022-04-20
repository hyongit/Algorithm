# 백준 [N-Queen]
# 백트래킹 : break나 continue해서 불필요한 재귀 호출을 줄임

n = int(input())
row = [0] * n
visited = [0] * n

result = 0

def dfs(depth):
    global result

    if depth == n: # 종료 조건, depth가 n까지 갔을 때
        result += 1
        return

    for i in range(n):
        # 자리에 Queen이 존재하는지 확인
        if visited[i] == 0 :    
            row[depth] = i

            pos = True
            # depth만큼 for문 돌리면서 대각선에 Queen이 존재 검사 --> 존재 시 break, 존재하지 않으면 depth 늘려 탐색
            for j in range(depth):
                # 대각선 존재 여부 : 행 차이 == 열 차이
                if abs(depth - j) == abs(row[depth] - row[j]):
                    pos = False
                    break

            # 중복 없을 시
            if pos :
                visited[i] = True
                dfs(depth + 1)
                visited[i] = 0


dfs(0)
print(result)