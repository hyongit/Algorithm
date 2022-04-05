# 백준 [프린터 큐]
# 큐
from collections import deque

case = int(input())

for _ in range(case):
    n, m = map(int, input().split())
    printList = list(map(int, input().split()))
    checkList = [0 for _ in range(n)]
    checkList[m] = 1
    
    #print(checkList)
    count = 1

    while True:
        if printList[0] == max(printList):

            if checkList[0] == 1:
                print(count)
                break

            else :
                printList.pop(0)
                checkList.pop(0)
                count+=1
        else:
            checkList.append(checkList[0])
            printList.append(printList[0])
            printList.pop(0)
            checkList.pop(0) 

    

