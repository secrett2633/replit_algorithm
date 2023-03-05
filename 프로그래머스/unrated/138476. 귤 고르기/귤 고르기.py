def solution(k, tangerine):
    answer = 0
    arr = {}
    for i in tangerine:
        try: arr[i] += 1
        except: arr[i] = 1
    arr = sorted(list(arr.values()))
    while k > 0:
        k -= arr.pop()
        answer += 1
    return answer