# [백준] 문서 검색

a = input()
b = input()
res = 0

while True:
    # find는 문자나 문자열이 처음으로 나온 위치를 알려주는 함수
    # 없으면 -1 반환
    idx = a.find(b)

    if idx == -1: 
        break

    res += 1
    a = a[idx + len(b):]

print(res)

