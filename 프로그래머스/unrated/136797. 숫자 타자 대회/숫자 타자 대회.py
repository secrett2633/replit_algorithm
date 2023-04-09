def solution(numbers):
    answer = 0
    arr = {"1" : [0, 0], "2" : [0, 1], "3" : [0, 2], "4" : [1, 0], "5" : [1, 1], "6" : [1, 2], "7" : [2, 0], "8" : [2, 1], "9" : [2, 2], "0" : [3, 1]}
    left, right = [1, 0], [1, 2]
    
    def solve(x1, y1, target):
        a = abs(x1 - target[0])
        b = abs(y1 - target[1])
        return max(1, min(a, b) * 3 + (max(a, b) - min(a, b)) * 2)
    
    import heapq
    q = [[0, 1, 0, 1, 2]]
    for target in numbers:
        tmp = []
        visited = []
        while q:
            cnt, x1, y1, x2, y2 = heapq.heappop(q)
            if (x1, y1) == (x2, y2): continue
            if [x1, y1, x2, y2] in visited: continue
            visited.append([x1, y1, x2, y2])
            heapq.heappush(tmp, [cnt + solve(x1, y1, arr[target])] + arr[target] + [x2, y2])
            heapq.heappush(tmp, [cnt + solve(x2, y2, arr[target])] + [x1, y1] + arr[target])
        q = tmp         
    return heapq.heappop(q)[0]
    return answer