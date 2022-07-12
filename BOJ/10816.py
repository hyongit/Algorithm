# [백준] 숫자 카드2
# 이분 탐색

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

arr.sort()
arrDict = {}

ans_list = []

for a in arr:
    if a not in arrDict:
        # 없으면 딕셔너리에 삽입
        arrDict[a] = 1 # 딕셔너리명[key] = value, {-10: 1}

    else:
        # 있으면, value 값만 올려줌
        arrDict[a] += 1 # {-10: 2}      

# arrDict : {-10: 2, 2: 1, 3: 2, 6: 1, 7: 1, 10: 3}

def binary_search(target):
    start = 0
    end = n-1

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == target:
            # return 값을 target의 value 값으로
            return arrDict[target]
        elif arr[mid] < target:
            start = mid+1
        else:
            end = mid-1
    return 0

for i in arr2:
    ans = binary_search(i)
    ans_list.append(ans)

print(' '.join(map(str, ans_list)))

# print(arrDict[-10]) 2
for v in arrDict.values():
    print(v)
