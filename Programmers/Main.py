money = 4578
costs = [1, 4, 99, 35, 50, 1000]
won = [1, 5, 10, 50, 100, 500]

costs = costs[::-1]
won = won[::-1]
ans = []

for i in range(len(costs)):
    mok = 0
    k = 0
    arr = []
    mok = money // won[i]
    k = won[i] * mok

    for j in range(len(costs)):
        tmp = k // won[j]
        c = costs[j] * tmp
        if c != 0:
            arr.append(c)

    print(arr)
    if len(arr) >= 1:
        ans.append(min(arr))
    money %= won[i]

print(ans)