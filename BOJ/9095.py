# [백준] 1,2,3 더하기
# DP

t = int(input())

def dynamic(num):
    if num == 1:
        return 1

    elif num == 2:
        return 2

    elif num == 3:
        return 4
    
    else:
        return dynamic(num-1) + dynamic(num-2) + dynamic(num-3)

for _ in range(t):
    n = int(input())
    print(dynamic(n))