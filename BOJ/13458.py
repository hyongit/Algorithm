# 백준 [시험 감독]
# while문 쓰면 시간초과, 사칙연산으로 풀기

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

# n = 3
# a = [3, 4, 5]
# b, c = 2, 2

answer = 0

for i in range(n):
    a[i] -= b
    answer += 1

    if a[i] > 0:
        if a[i] >= c:
            if a[i] % c == 0:
                answer += (a[i] // c)
            else:
                answer += (a[i] // c) + 1
                
        else:
            answer += 1
    
    
print(answer)