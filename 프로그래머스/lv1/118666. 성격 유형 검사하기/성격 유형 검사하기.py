def solution(survey, choices):
    answer = ''
    arr = [0, 0, 0, 0]
    flag = {"RT" : [1, 0, 0, 0], "TR" : [-1, 0, 0, 0], "CF" : [0, 1, 0, 0], "FC" : [0, -1, 0, 0], "JM" : [0, 0, 1, 0], "MJ" : [0, 0, -1, 0], "AN" : [0, 0, 0, 1], "NA" : [0, 0, 0, -1]}
    for i in range(len(survey)):
        arr = [a + (choices[i] - 4) * b for a, b in zip(arr, flag[survey[i]])]
    for i, a in enumerate([["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]):
        answer += a[0] if arr[i] <= 0 else a[1]
    return answer