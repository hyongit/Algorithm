# [백준] 나무 자르기

n, m = map(int, input().split())
h = list(map(int, input().split()))
h.sort()

answer = 0


start = 1
end = max(h)
answer = 0

while start <= end :
    mid = (start+end)//2
    temp = 0

    # 잘린 나무의 합 구함
    # 나무 높이 for문 돌리면서 mid보다 크면 temp에 더해줌
    for tree in h: 
        if tree >= mid:
            temp += tree-mid

    if temp == m: # 잘린 나무의 합이 m과 일치하면 끝
        answer = mid
        break

    elif temp > m: # 잘린 나무의 합이 m보다 크면 mid가 정답 가능성 있기에 answer에 일단 대입
        answer = mid
        start = mid+1 # start를 mid 다음으로

    else: # 잘린 나무의 합이 mid보다 작으면 mid 정답 가능성 X
        end = mid-1 # end를 mid 전으로

print(answer)
