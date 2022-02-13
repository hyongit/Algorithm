# 가장 작은 것을 선택해 맨 앞과 바꾸고
# 그 다음 작은 데이터를 선택해 앞에서 두 번째 것과 바꾸는 식
# 가장 작은 것을 선택한다는 의미에서 선택 정렬
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스와프

print(array)
