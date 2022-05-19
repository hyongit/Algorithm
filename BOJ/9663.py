# 백준 [N-Queen]
# 백트래킹 : break나 continue해서 불필요한 재귀 호출을 줄임

# n = int(input())
n = 8
answer = 0

row = [0] * n
visit = [0] * n

def recur(num):
    global answer

    if num == n:
        answer += 1
        return
    
    for i in range(n):
        # 방문 안한 것 확인
        if visit[i] == 0:
            # Queen 놓기
            row[num] = i

            pos = True

            # 깊이 만큼 for문 돌리면서 대각선에 Queen 존재 여부 검사 
            # --> 존재 시 break, 존재하지 않으면 깊이 늘려서 탐색
            for j in range(num):
                # 대각선 존재 여부 절댓값 행 차이 == 절댓값 열 차이 
                if abs(num - j) == abs(row[num] - row[j]) :
                    pos = False
                    break
            
            # 대각선 중복 없을 시 
            if pos:
                #방문 처리
                visit[i] = 1
                recur(num+1)
                visit[i] = 0


recur(0)
print(answer)