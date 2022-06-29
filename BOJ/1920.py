# 백준 [수 찾기]
# 이진 탐색

n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))
ans = []

a_list.sort()

def binary_search(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2
        if a_list[mid] == target:
            return 1
        elif a_list[mid] > target:
            end = mid-1
        else:
            start = mid+1

for i in m_list:
    if binary_search(i) == 1:
        ans.append(1)
    else:
        ans.append(0)

for a in ans:
    print(a)