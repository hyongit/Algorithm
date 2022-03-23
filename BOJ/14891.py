# 백준 [톱니바퀴]

from collections import deque

#rotate 함수 써야하므로 deque 4개 받음
gear = [deque(map(int, input())) for _ in range(4)]
k = int(input())
orders = deque(list(map(int, input().split())) for _ in range(k)) # 덱에 리스트 2개 (gear 번호랑 방향)
result = 0

while orders: # 덱에 아무것도 없을 때까지만
    num, d = orders.popleft()
    num -= 1 # 리스트 인덱스 맞춰주기
    tmp_2 = gear[num][2]
    tmp_6 = gear[num][6]
    gear[num].rotate(d) # 일단 지금 기어 회전!
    tmp_direct = d

    # 왼쪽 확인
    for i in range(num-1, -1, -1):
        if tmp_6 != gear[i][2]:
            tmp_6 = gear[i][6]  # 이 기어의 6번 일단 저장
            gear[i].rotate(d * -1) # 방향 바꿔서 rotate
            d *= -1 # 바꾼 방향 저장
        else:
            break

    d = tmp_direct # 왼쪽 확인하면서 d가 바뀌었을 수도 있으니
    # 오른쪽 확인
    for i in range(num+1, 4):
        if tmp_2 != gear[i][6]:
            tmp_2 = gear[i][2]
            gear[i].rotate(d * -1)
            d *= -1
        else:
            break

# 점수 출력
for i in range(4):
    if gear[i][0] == 1:
        result += 2**i

print(result)