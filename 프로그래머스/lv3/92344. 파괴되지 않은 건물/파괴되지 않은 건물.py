def solution(board, skill):
    answer = 0
    arr = [[0] * (len(board[0]) + 1) for _ in range((len(board) + 1))]
    tmp = {1 : -1, 2 : 1}
    for t, x1, y1, x2, y2, d in skill:
        x2 += 1
        y2 += 1
        arr[x2][y2] += tmp[t] * d
        arr[x2][y1] -= tmp[t] * d
        arr[x1][y2] -= tmp[t] * d
        arr[x1][y1] += tmp[t] * d
    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[i][j + 1] += arr[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            arr[i + 1][j] += arr[i][j]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if arr[i][j] + board[i][j] >= 1: 
                answer += 1    
    return answer