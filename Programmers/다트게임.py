import sys

dartResult = sys.stdin.readline().strip()
tmp = []
k = ""
for i in dartResult:
    k += i

    if k.isdigit() == True:
        pass
    elif k.isalnum() == True:
        if k[:-1] == '10':
            if k[2] == 'S':
                k = 10
            elif k[2] == 'D':
                k = 100
            elif k[2] == 'T':
                k = 1000
            tmp.append(int(k))
            k = ""

        else:
            if k[1] == 'S':
                k = int(k[0])
            elif k[1] == 'D':
                k = int(k[0]) * int(k[0])
            elif k[1] == 'T':
                k = int(k[0]) * int(k[0]) * int(k[0])

            tmp.append(int(k))
            k = ""
    else:
        if k == '*':
            if len(tmp) == 1:
                tmp[0] *= 2
            else:
                tmp[-2] *= 2
                tmp[-1] *= 2
        elif k == '#':
            tmp[-1] *= -1
        k = ""

print(sum(tmp))
