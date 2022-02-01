def solution(board, moves):
    tmp = []
    result = []

    for move in moves:
        for i in range(len(board)):
            if board[i][move - 1] > 0:
                tmp.append(board[i][move - 1])
                board[i][move - 1] = 0

                if tmp[-1:] == tmp[-2:-1]:
                    result.append(tmp[-2:])
                    tmp = tmp[:-2]
                break

    return len(result) * 2

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))