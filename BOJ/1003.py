# [백준] 피보나치 함수
# 다이나믹 프로그래밍
import sys
input = sys.stdin.readline

n = int(input().strip())

# fibo(num-1)의 0, 1의 호출 횟수 + fibo(num-2)의 0, 1의 호출 횟수 = fibo(num)의 0, 1의 호출 횟수
zero = [1, 0, 1]
one = [0, 1, 1]

# zero : [1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...]
# one : [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...]

def fibo(num):
    length = len(zero)

    if num >= length:
        for i in range(length, num+1):
            zero.append(zero[i-1] + zero[i-2])
            one.append(one[i-1] + one[i-2])

    print(zero[num], one[num])
    

for _ in range(n):
    t = int(input().strip())
    fibo(t)