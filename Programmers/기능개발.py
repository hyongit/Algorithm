# [프로그래머스] 기능개발

progresses = [55, 60, 65]
speeds = [5, 10, 7]

answer = []

cnt = 0

while progresses:
    
    for i in range(len(progresses)):
        progresses[i] += speeds[i]

    # progresses의 길이가 0보다 크고, progresses의 첫번째 원소가 100보다 클 때만 while문 돌림
    while len(progresses) > 0 and progresses[0] >= 100:
        progresses.pop(0)
        speeds.pop(0)
        cnt+=1

    if cnt != 0:           
        answer.append(cnt)
        cnt = 0
        
print(answer)
