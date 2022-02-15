#파라메트릭 서치, 이진탐색, 반복문
n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = 0
end = max(arr)

result = 0
while (start <= end) :
    sum = 0
    mid = (start + end) // 2

    for i in arr:
        if i > mid:
            sum += i - mid

    if sum < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)