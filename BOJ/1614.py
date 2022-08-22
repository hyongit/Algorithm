# [백준] 영식이의 손가락

finger = int(input())
cnt = int(input())

if 2<=finger<=4:
    print(cnt/2*8)
elif finger == 1:
    print(cnt * 8)
else:
    print(cnt*8 + 4)