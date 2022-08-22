# [백준] 문자열
# 브루트포스

a, b = input().split()
cnt_list = []

for i in range(len(b)-len(a)+1):
    cnt = 0
    for j in range(len(a)):
        if a[j] != b[i+j]:
            cnt+=1
    cnt_list.append(cnt)

print(min(cnt_list))