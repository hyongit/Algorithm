# [백준] 최대 힙
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
        print(abs(que.get())) # 출력할 때는 절댓값으로 부호 바꿔서 출력
    else:
        que.put(-x) # 최대 힙 만들기 위해 부호 반대로 저장

# input:  1, 2
# que: [-2, -1]