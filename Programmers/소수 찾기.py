# [프로그래머스] 소수 찾기 (level 2)

from itertools import permutations

def sosu(n):
    if n < 2:
        return False
    else:
        for i in range(2, n//2+1):
            if n%i==0:
                return False
    return True

def solution(numbers):
    answer = []
    nums = [k for k in numbers]
    tmp = []
    new_nums = []
    
    for i in range(1, len(nums)+1):
        tmp += list(permutations(nums, i))
    
    
    for j in range(len(tmp)):
        if int(''.join(tmp[j])) not in new_nums:
            new_nums.append(int(''.join(tmp[j])))
                   
    for x in range(len(new_nums)):
        if sosu(new_nums[x]) == True: 
            print(new_nums[x])
            answer.append(new_nums[x])
    
    return len(answer)