def solution(numbers):
    answer = 0
    arr = {"1" : [0, 0], "2" : [0, 1], "3" : [0, 2], "4" : [1, 0], "5" : [1, 1], "6" : [1, 2], "7" : [2, 0], "8" : [2, 1], "9" : [2, 2], "0" : [3, 1]}
    left, right = [1, 0], [1, 2]
    
    def solve(now, target):
        a = abs(now[0] - target[0])
        b = abs(now[1] - target[1])
        return max(1, min(a, b) * 3 + (max(a, b) - min(a, b)) * 2)
    
    dp = [[[0, 1, 0, 1, 2], [0, 1, 0, 1, 2]]] + [[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0]] for _ in range(len(numbers))]
    for i in range(len(numbers)):
        tmp = solve(dp[i][0][1:3], arr[numbers[i]])
        tmp1 = solve(dp[i][1][1:3], arr[numbers[i]])
        # if dp[i][0][0] + tmp 
        # dp[i + 1][1]
        print(tmp, tmp1)
        
    return answer