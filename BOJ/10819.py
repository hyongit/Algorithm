# 백준 [차이를 최대로]

#from itertools import permutations

n = int(input())
nums = list(map(int, input().split()))

max_num = -int(1e9)
arr = []
visit = [0 for _ in range(n)]

def calc(lst):
    global max_num
    tmp = 0

    for i in range(n-1):
        tmp += abs(lst[i] - lst[i+1])

    if max_num < tmp:
        max_num = tmp


# 순열 구하는 라이브러리
# for i in permutations(nums, 6):
#     print(i)
    
    
def recur(d):

    if len(arr) == n:
        #print(arr)
        calc(arr)
        return
    
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1

            arr.append(nums[i])
        
            recur(d+1)

            # for문 끝까지 돌려야 된다는 것 유의 !!
            visit[i] = 0
            arr.pop()

recur(0)
print(max_num)