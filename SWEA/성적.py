n, m = map(int, input().split())
arr = list(map(int, input().split()))

for _ in range(m):
    a, b = map(int, input().split())
    asum = 0

    for i in range(a-1, b):
        asum += arr[i]
    
    print('%.2f' % (asum/(b-a+1)))