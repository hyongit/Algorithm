# 백준 [로또]
# 백트래킹

def recur(num):

    if len(answer) == 6:
        print(' '.join(map(str, answer)))
        return

    for i in range(num, k):
        answer.append(s[i])
        recur(i+1)
        answer.pop()


while True:
    nums = list(map(int, input().split()))
    k = nums[0]
    s = nums[1:]
    s.sort()

    answer = []

    if k == 0:
        break

    recur(0)
    print()