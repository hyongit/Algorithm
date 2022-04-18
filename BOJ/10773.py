# 백준 [제로]
# 구현
import sys

input = sys.stdin.readline

n = int(input())
k = []
stack = []

for _ in range(n):
    tmp = int(input())
    k.append(tmp)

for i in k:
    if i == 0:
        stack.pop()
    else:
        stack.append(i)

print(sum(stack))