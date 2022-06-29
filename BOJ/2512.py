# [백준] 예산

n = int(input())
budget = list(map(int, input().split()))
m = int(input())

start = 0
end = max(budget)

while start <= end:
    mid = (start+end)//2
    total = 0

    for i in budget:
        if i >= mid:
            total += mid
        else:
            total += i
        
        #print(total)
    
    if total <= m:
        start = mid+1
    else:
        end = mid-1

    print('mid, total, start, end :', mid, total, start, end)

print(end)
