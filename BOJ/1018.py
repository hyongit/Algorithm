# 백준 [ 체스판 다시 칠하기 ]

n, m = map(int, input().split())
board = []

for i in range(n):
    board.append(input())

mini = []

# 8*8로 잘라내야 하므로 행 n-7, 열 m-7의 for문 돌림
for i in range(n - 7):
    for j in range(m - 7):
				# 첫 번째 칸의 문자가 ‘W’인 경우와 ‘B’인 경우 다시 칠해야 하는 최솟값 둘 다 계산
        first_w = 0
        first_b = 0
        for l in range(i, i+8):
            for k in range(j, j+8):
                if (l+k) % 2 == 0:
										# 첫 번째 칸의 문자(l+k가 짝인 곳)가 W인 경우
                    if board[l][k] != 'W' : first_w += 1 
										# 첫 번째 칸의 문자(l+k가 짝인 곳)가 B인 경우
                    if board[l][k] != 'B' : first_b += 1 
                else:
                    if board[l][k] != 'B' : first_w += 1
                    if board[l][k] != 'W' : first_b += 1

				# mini 리스트에 다시 칠해야 하는 수 저장
        mini.append(first_w)
        mini.append(first_b)

print(min(mini))