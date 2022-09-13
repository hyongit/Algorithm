# [프로그래머스] 이진 변환 반복하기

s = '1111111'
s_new = ''
zero = 0
cnt = 0

while True:

    if s == '1':
        break

    for k in s:
        if k == '0':
            zero += 1
            continue
        else:
            s_new += k
    
    s = bin(len(s_new))[2:]
    s_new = ''
    cnt+=1    
    

print(cnt, zero)
        