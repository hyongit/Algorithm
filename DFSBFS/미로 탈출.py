import sys
from collections import deque
#최단 경로 구하는 문제, BFS로 탐색
#거리는 그래프 값에다 증가

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().strip())))


# def bfs(x, y):
#
#
# print(bfs(0,0))