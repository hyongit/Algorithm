# 백준 [제로]
# 구현
import sys
input = sys.stdin.readline

k = int(input())
stk = []
answer = []

for _ in range(k):
    n = int(input())
    stk.append(n)

# i가 0이 아니면 append하고 0이면 pop
for i in stk:
    if i == 0:
        answer.pop()
    else:
        answer.append(i)

print(sum(answer))
