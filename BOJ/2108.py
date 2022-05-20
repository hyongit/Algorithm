# 백준 [통계학]
import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
nums = []

dic = []
max_bin = 0

for _ in range(n):
    num = int(input())
    nums.append(num)

set_nums = list(set(nums))

# 평균
s = int(sum(nums))

if s < 0:
    print(int((sum(nums)/n) - 0.5))
elif s >= 0:
    print(int((sum(nums)/n) + 0.5))

# 중앙값
print(sorted(nums)[n//2])

max_bin = Counter(nums).most_common()

max_bin.sort(key= lambda x : (-x[1], x[0]))

if len(max_bin) > 1 and max_bin[0][1] == max_bin[1][1]:
    print(max_bin[1][0])
else:
    print(max_bin[0][0])

#print(max_bin)

# 범위
print(max(nums)-min(nums))
