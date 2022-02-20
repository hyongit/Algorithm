from bisect import bisect_left, bisect_right
import sys

n, m = map(int, input().split())
array = list(map(int, sys.stdin.readline().strip().split()))

def count_by_range(arr, a, b):
    a = bisect_right(arr, a)
    b = bisect_left(arr, b)
    return a - b

#값이 m인 데이터의 개수를 출력
if m in array:
    print(count_by_range(array, m, m))
else:
    print(-1)