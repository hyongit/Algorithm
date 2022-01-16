######## [이코테] 모험가 길드 ########
n = int(input())
data = list(map(int,input().split()))
data.sort()

cnt = 0
result = 0

for i in data: # 오름차순으로 하나씩 확인
    cnt += 1 #모험가 한 명 넣기
    if cnt >= i: #현재 cnt에 들어 있는 모험가 수 >= 공포도 수 이면 여행 보내기!
        result += 1
        cnt = 0 #다음 비교를 위해 여행 보냈으면 cnt를 초기화

print(result)
