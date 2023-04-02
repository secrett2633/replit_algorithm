def solution(scores):
    scores = [[a, b, i] for i, (a, b) in enumerate(scores)]
    scores.sort(reverse = True)
    q = []
    cnt = [int(1e9), -1, -1] #과거 a 값, 과거 b 최대값, 현재 b 값
    '''
    과거 a 값이랑 현재 a값이랑 비교했을때
    값이 같다면 과거 b 최대값이랑 비교하고
    값이 다르다면(현재 a값이 과거 a값보다 작아지는경우)일떄
    과거 b최대값이랑 현재 b값의 최대값으로 설정하고 이거랑 비교
    현재 b값을 계속 최대값으로 두어야함
    '''   
    for a, b, i in scores:
        if a != cnt[0]: 
            cnt = [a, max(cnt[1], cnt[2]), b]
        if b < cnt[1]: continue            
        cnt[2] = max(cnt[2], b)
        q.append([a + b, i])
    q.sort(key = lambda x : (int(1e9) - x[0], x[1]))
    for i, (a, b) in enumerate(q):
        if b == 0: return i + 1
    return -1