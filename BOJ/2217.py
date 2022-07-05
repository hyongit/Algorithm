# [백준] 로프
# 그리디, 정렬

n = int(input())
arr = []
ans = []

for i in range(n):
    k = int(input())
    arr.append(k)

arr.sort(reverse=True)

# 선택한 로프 뒤에 있는 로프의 갯수만큼 곱해줘야 함
for j in range(n):
    ans.append(arr[j]*(j+1))

print(max(ans))