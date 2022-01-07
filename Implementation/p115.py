########## [이코테] 왕실의 나이트 ##########
n = list(input())
steps = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (1, -2), (-1, 2), (1, 2)]
x, y = ord(n[0])-96, int(n[1])
cnt = 0

for i in range(len(steps)):
    nx = x + steps[i][0]
    ny = y + steps[i][1]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        pass
    else:
        cnt += 1

print(cnt)

''' 알파벳 문자 -> 해당 알파벳의 순서 숫자로 바꾸는 법
대문자 : (int(ord(str)) - int(ord('A'))) + 1
소문자 : (int(ord(str)) - int(ord('a'))) + 1'''

