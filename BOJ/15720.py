# [백준] 카우버거

b, c, d = map(int, input().split())
cnt = min(b, c, d)

b_list = list(map(int, input().split()))
c_list = list(map(int, input().split()))
d_list = list(map(int, input().split()))

b_list.sort(reverse=True)
c_list.sort(reverse=True)
d_list.sort(reverse=True)

ans = 0

for i in range(cnt):
    tmp = (b_list[i] + c_list[i] + d_list[i]) * 0.9
    ans+=int(tmp)
 
if b > cnt:
    for i in range(cnt, b):
        ans += b_list[i]

if c > cnt:
    for i in range(cnt, c):
        ans += c_list[i]

if d > cnt:
    for i in range(cnt, d):
        ans += d_list[i]

print(sum(b_list) + sum(c_list) + sum(d_list))
print(ans)