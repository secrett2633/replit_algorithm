def solution(triangle):
    answer = 0
    res = [[0] * (len(triangle) + 1) for _ in range(len(triangle) + 1)]
    res[0][0] = triangle[0][0]
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            res[i + 1][j] = max(res[i + 1][j], res[i][j] + triangle[i + 1][j])
            res[i + 1][j + 1] = max(res[i + 1][j + 1], res[i][j] + triangle[i + 1][j + 1])
    answer = max(res[len(triangle) - 1])   
    return answer