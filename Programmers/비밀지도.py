n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

tmp1 = []
tmp2 = []


new_tmp = []

for i in range(n):
    tmp1.append(bin(arr1[i]).replace('b', ''))
    if len(tmp1[i]) > n:
        tmp1[i] = tmp1[i][1:]
    elif len(tmp1[i]) < n:
        while len(tmp1[i]) < n:
            tmp1[i] = '0' + tmp1[i]

    tmp2.append(bin(arr2[i]).replace('b', ''))
    if len(tmp2[i]) > n:
        tmp2[i] = tmp2[i][1:]
    elif len(tmp2[i]) < n:
        while len(tmp2[i]) < n:
            tmp2[i] = '0' + tmp2[i]

for i in range(len(tmp1)):
    k = ""
    for j in range(len(tmp1[i])):
        if tmp1[i][j] == '0' and tmp2[i][j] == '0' :
            k += ' '
        elif tmp1[i][j] == '1' and tmp2[i][j] == '1':
            k += '#'
        else:
            k += '#'
    new_tmp.append(k)


print(new_tmp)