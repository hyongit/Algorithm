left = 13
right = 17

sum = 0

for i in range(left, right+1):
    arr = [1]
    for j in range(2, i+1) :
        if i%j == 0:
            arr.append(j)

    if len(arr)%2 == 0:
        sum+=i
    else:
        sum-=i

print(sum)