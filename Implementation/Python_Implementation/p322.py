########## [이코테] 문자열 재정렬 ##########
str = list(input())
alp = []
num = []
for i in str:
    if i.isalpha(): #문자인지 확인
        alp.append(i)
    else:
        num.append(int(i))

alp.sort()
print(''.join(alp), end='')
if num: #숫자가 존재 한다면
    print(sum(num))

'''정답을 보니 num을 변수로 해도 됐었음...
문자면 똑같이 리스트에 넣고, 숫자면 변수에 더하는 식으로
그리고 숫자가 0이 아니면 리스트 가장 뒤에 삽입하여 출력!'''
