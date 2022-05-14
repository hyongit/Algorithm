# 백준 [ N과 M (4) ]
# 백트래킹

n, m = map(int, input().split())
answer = []

def recur(num):
    global k

    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(num, n+1):
        #print(num)
        answer.append(i)
        recur(i)
        answer.pop()

recur(1)