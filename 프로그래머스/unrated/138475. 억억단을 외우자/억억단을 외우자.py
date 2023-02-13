def solution(e, starts):
    answer = []
    
    arr = [0] * (e + 1)
    res = [0] * (e + 1)
    for i in range(2, e + 1):
        for j in range(i, e + 1, i):
            arr[j] += 1
    cnt = -1
    cnt1 = 0
    for j in range(e, min(starts) - 1, -1):
        if cnt <= arr[j]: cnt = arr[j]; cnt1 = j
        res[j] = cnt1
    return list(map(lambda x:res[x], starts))