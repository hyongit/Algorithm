# [백준] 크리스마스 선물
import heapq
n = int(input())
heap = []

for _ in range(n):
    a_list = list(map(int, input().split()))

    if a_list[0] == 0:
        if len(heap) == 0:
            print('-1')
        else:
            print(abs(heapq.heappop(heap))) # maxheap pop
    
    else:
        for i in range(1, len(a_list)):
            heapq.heappush(heap, -a_list[i])
