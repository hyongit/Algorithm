# [백준] 에라토스테네스의 체
# 구현

n, k = map(int, input().split())
#n, k = 15, 12
stk = []
num, cnt, ans = 0, 0, 0

for i in range(2, n+1):
    stk.append(i)

while stk:
    num = stk.pop(0)
    cnt+=1

    if cnt == k:
        print(num)
        break   

    for s in stk:
        if s % num == 0:
            ans = s
            stk.remove(s)
            cnt+=1

            if cnt == k:
                print(ans)
                break            
            
