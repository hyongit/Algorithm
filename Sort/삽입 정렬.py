#삽입 정렬 O(N^2)
# 데이터를 하나씩 확인, 각 데이터를 적절한 위치에 삽입
# 선택 정렬보다 효율적
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 1씩 감소하면서 반복
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)