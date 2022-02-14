arr = [5,7,9,0,3,1,6,2,4,8]

def quick_sort(arr):
    #리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr

    pivot = arr[0] #피벗은 첫 번째 원소
    tail = arr[1:] # 피벗을 제외한 리스트

    # pivot보다 작은 데이터들 다 모임
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 재귀로 left right 정렬
    return quick_sort(left_side) + [pivot] + quick_sort(right_side) 

print(quick_sort(arr))