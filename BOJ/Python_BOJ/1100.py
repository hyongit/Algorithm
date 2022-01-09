import sys
board = []
cnt = 0

for _ in range(8):
    cmd = sys.stdin.readline().strip()
    board.append(cmd)

for i in range(8): #행
    for j in range(8): #열
        if i % 2 == 0 and j % 2 == 0 and board[i][j] == 'F':
            cnt += 1
        if i % 2 == 1 and j % 2 == 1 and board[i][j] == 'F':
            cnt += 1
print(cnt)

''' 이걸 왜 어렵게 푼거지... 
체스판은 하얀 칸부터 시작 시 다음 칸은 검정 칸부터 시작한다는 것을 간과함...!!!

* 짝수 행일 때 짝수번째에 F가 있을 시 cnt 증가
* 홀수 행일 때 홀수번째에 F가 있을 시 cnt 증가 '''
