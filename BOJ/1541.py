# [백준] 잃어버린 괄호
# 그리디

str = input().split('-') # 55, 50+40
ans = 0

for i in str[0].split('+'):
    ans += int(i)

for i in str[1:]:
    for j in i.split('+'):
        ans -= int(j)

print(ans)