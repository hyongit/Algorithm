# 백준 [시리얼 번호]
# 정렬

n = int(input())
arr = []

for _ in range(n):
    num = input()
    arr.append(num)

def sum(str):
    a = 0

    for s in str:
        if s.isdigit() == True:
            a += int(s)
    return a

# 1. 길이 순 -> 2. 길이 같으면 sum(x) 값 순 -> 3. 길이도 같으면 사전 순
arr.sort(key = lambda x : (len(x), sum(x), x))

for a in arr:
    print(a)


