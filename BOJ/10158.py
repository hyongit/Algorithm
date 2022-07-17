# [백준] 개미
# 틀린 코드

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

w_list = []
h_list = []
np, nq = 0, 0

# w, h 리스트 생성
for i in range(w):
    w_list.append(i)
for j in range(w, 0, -1):
    w_list.append(j)

for i in range(h):
    h_list.append(i)
for j in range(h, 0, -1):
    h_list.append(j)

# 리스트의 [(초깃값 + 시간) % 길이] 번째 수
np = w_list[(p + t) % (2 * w)]
nq = h_list[(q + t) % (2 * h)]

print(np, nq)