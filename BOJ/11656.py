# [백준] 접미사 배열

s = input()
str = []

for i in range(len(s)):
    str.append(s[i:])

str.sort()

for j in range(len(str)):
    print(str[j])