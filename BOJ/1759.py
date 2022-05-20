# 백준 [암호 만들기]

l, c = map(int, input().split())
str = list(input().split())

# l, c = 4, 6
# str = ['a', 't', 'c', 'i', 's', 'w']
# a, c, i, s, t, w
str.sort()
password = []
all_out = []
idx = 0

# 백트래킹으로 오름차순 문자 조합 만들기
def recur(num, idx):

    if num == l:
        #print(''.join(password))
        all_out.append(''.join(password))
        return
    
    for i in range(idx, c):
        if str[i] not in password:
            password.append(str[i])
            recur(num+1, i+1)
            password.pop()

# 자음 모음 체크
def make_password(list_check):
    
    for i in list_check:
        cons = 0
        vow = 0 

        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow +=1

        if cons >= 1 and vow >= 2:
            print(i)


recur(0, idx)
make_password(all_out)