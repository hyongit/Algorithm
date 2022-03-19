import sys

n = int(input())
arr = list(map(int, sys.stdin.readline().strip().split()))
b, c = map(int, input().split())

answer = 0

for i in arr:
    i -= b
    answer += 1

    if i > 0:
        if i < c:
            answer+=1
            continue
        else:
            if i % c == 0:
                answer += i//c
            else:
                answer += i//c
                answer += 1
    else:
        continue

print(answer)