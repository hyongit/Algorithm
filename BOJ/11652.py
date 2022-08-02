# [백준] 카드
# 정렬
import sys

input = sys.stdin.readline

n = int(input())
card = dict()

for i in range(n):
    num = int(input().strip())

    if num in card:
        card[num] += 1
    else:
        card[num] = 1

card.items().sort(key = lambda x : (-x[1], x[0]))
#answer = sorted(card.items(), key = lambda x : (-x[1], x[0]))
print(answer[0][0])
