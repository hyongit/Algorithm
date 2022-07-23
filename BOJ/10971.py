# [백준] 외판원 순회 2

# n = 4
# maps = [[0, 10, 15, 20], [5, 0, 9, 10], [6, 13, 0, 12], [8, 8, 9, 0]]
#maps = [[0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1], [1, 0, 0, 0]]
n = int(input())
maps = [list(map(int, input().split())) for _ in range(n)]

ans = []
answer = 1e9
cost = 0

def recur(cost):
    global answer

    if len(ans) == n:
        
        print(ans)
        if maps[ans[-1]][ans[0]] > 0:
            cost += maps[ans[-1]][ans[0]]
            print(cost)
            if answer > cost:
                answer = cost
        return
        

    else:
        for i in range(n):
            if not ans:
                if i == 1:
                    return
                ans.append(i)
                recur(cost)
                ans.pop()

            elif i not in ans and maps[ans[-1]][i] > 0:
                ans.append(i)
                cost += maps[ans[-2]][ans[-1]]
                recur(cost)
                cost -= maps[ans[-2]][ans[-1]]
                ans.pop()
        

recur(0)
print(answer)
