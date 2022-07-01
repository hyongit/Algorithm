# [백준] 1,2,3 더하기
# DP

n = int(input())
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

def dynamic(x):

    if x == 1:
        return 1
    
    elif x == 2:
        return 2
    
    elif x == 3:
        return 4
    
    else:
        return dynamic(x-1) + dynamic(x-2) + dynamic(x-3)

for i in nums:
    print(dynamic(i))    