# [백준] 최소힙
# 우선순위 큐

from queue import PriorityQueue
import sys

input = sys.stdin.readline

que = PriorityQueue()

n = int(input())

for _ in range(n):
    x = int(input().strip())

    if x == 0 and que.empty():
        print(0)
    elif x == 0:
        print(que.get())
    else:
        que.put(x)
    