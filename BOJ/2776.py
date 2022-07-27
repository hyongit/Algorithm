# [백준] 암기왕

t = int(input())


def binary_search(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2

        if note1[mid] == target:
            return 1
        elif note1[mid] > target:
            end = mid-1
        else:
            start = mid+1
       
    return 0

for _ in range(t):
    n = int(input())
    note1 = list(map(int, input().split()))
    m = int(input())
    note2 = list(map(int, input().split()))

    note1.sort()

    for i in note2: 
        print(binary_search(i))