# [백준] 절댓값 힙

import heapq
import sys

input = sys.stdin.readline

n = int(input())
h = []

for _ in range(n):
    x = int(input().strip())

    if x == 0 and not h:
        print(0)
    elif x == 0:
        print(heapq.heappop(h)[1])
    else:
        # [(1, -1), (1, -1), (1, 1), (2, -2)] 절댓값, 원래 x값 같이 저장
        heapq.heappush(h, (abs(x), x)) 
    
    print(h)