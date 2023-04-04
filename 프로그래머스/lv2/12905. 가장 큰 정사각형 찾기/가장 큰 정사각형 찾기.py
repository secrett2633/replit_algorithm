def solution(board):
    answer = 0
    dp = [[0] * len(board[0]) for _ in range(len(board))]    
    dp[0] = board[0]
    for x in range(len(board)): dp[x][0] = board[x][0]
    for x in range(len(dp)):
        for y in range(len(dp[0])):
            if x > 0 and y > 0 and board[x][y] == 1:            	
                dp[x][y] = min(dp[x][y - 1], dp[x - 1][y], dp[x - 1][y - 1]) + 1
    for i in range(len(dp)): answer = max(answer, max(dp[i]))
    return answer * answer