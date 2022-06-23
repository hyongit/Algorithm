# 백준 [동전 0]
# 브루트포스

n, k = map(int, input().split())
money = []
ans = 0

for i in range(n):
    tmp = int(input())
    money.append(tmp)

while k > 0 :

    arr = []

    for i in range(n):
        if k < money[i]:
            break

        tmp = k // money[i]
        arr.append(tmp)
    
    k = k % money[len(arr)-1]
    ans += arr[-1]

    #print(k, ans)

print(ans)