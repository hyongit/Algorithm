# [백준] 단어 뒤집기2

s = input()

flag = False
tmp = ''
ans = ''

for i in s:
    if flag == False:
        if i == '<':
            flag = True
            tmp += i
        elif i == ' ':
            tmp += i
            ans += tmp
            tmp = ''
        else:
            tmp = i + tmp # 거꾸로 저장

    else:
        tmp += i
        if i == '>':
            flag = False
            ans += tmp
            tmp = ''
            
# 마지막 tmp는 공백이 없으므로 ans에 삽입 안됨, 더해서 출력
print(ans + tmp) 
    

