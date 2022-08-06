# [프로그래머스] 타겟 넘버
numbers = [4, 1, 2, 1]
target = 2

n = len(numbers)
answer = 0

def dfs(idx, result):
    global answer 
    if idx == n:
        if result == target:
            answer += 1
        return
    else:
        dfs(idx+1, result+numbers[idx])
        dfs(idx+1, result-numbers[idx])

dfs(0,0)
print(answer)