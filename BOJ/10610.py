# [백준] 30
# 문자열

str = input()
arr = []

for i in str:
    arr.append(i)

arr.sort(reverse=True)

if int(''.join(arr)) % 30 == 0:
    print(''.join(arr))
else:
    print(-1)

