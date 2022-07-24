# [백준] 사탕 게임
# 구현
import sys
input=sys.stdin.readline

n = int(input())
candy = [list(input()) for _ in range(n)]

answer = 0

def count(arr):
    result = 1
    
    for i in range(n):
        # 열 순회하며 연속하는 사탕 세기
        cnt = 1
        for j in range(1, n):
            if arr[i][j] == arr[i][j-1]:
                # 같으면 cnt+1
                cnt += 1
            else:
                # 다르면 다시 cnt 1로
                cnt = 1

            # cnt가 result보다 크면 변경
            if cnt > result:
                result = cnt
    

        # 행 순회하며 연속하는 사탕 세기
        cnt = 1
        for j in range(1, n):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1
        
            if cnt > result:
                result = cnt

    return result

for i in range(n):
    for j in range(n):
        # 열 바꾸기
        if j >= 1:
            candy[i][j-1], candy[i][j] = candy[i][j], candy[i][j-1]
            
            temp = count(candy)
            if temp > answer:
                answer = temp

            candy[i][j-1], candy[i][j] = candy[i][j], candy[i][j-1]
        

        # 행 바꾸기
        if i >= 1:
            candy[i-1][j], candy[i][j] = candy[i][j], candy[i-1][j]

            temp = count(candy)
            if temp > answer:
                answer = temp

            candy[i-1][j], candy[i][j] = candy[i][j], candy[i-1][j]

print(answer)
