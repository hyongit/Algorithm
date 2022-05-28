# 백준 [ 요세푸스 문제 0 ]
# k-1번째 사람들까지 앞에서부터 제거하여 뒤에 삽입
# k번째 사람 제거

from collections import deque

n, k = map(int, input().split())
q = deque()
answer = []

for i in range(1, n+1):
    q.append(i)

while q:
    for i in range(k-1):
        q.append(q.popleft())
    answer.append(q.popleft())

#print(answer)

print('<', end='')
print(', '.join(map(str, answer)), end='')
print('>', end='')
