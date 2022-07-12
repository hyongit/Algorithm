# [백준] 숫자 카드
# 이분 탐색

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))
ans_list = []

arr.sort()

def binary_search(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end)//2

        if arr[mid] == target:
            return 1
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    
    return 0

for i in arr2:
    ans = binary_search(i)
    ans_list.append(ans)

print(' '.join(map(str, ans_list)))