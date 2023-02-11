def solution(info, query):
    from bisect import bisect_left
    answer = []
    arr = [[[[[] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(3)]
    tmp = {"cpp": 0, "java": 1, "python": 2, "backend": 0, "frontend": 1, "junior": 0, "senior": 1, "chicken": 0, "pizza": 1}
    #[언어 3개][직군 2개][경력 2개][푸드 2개] = 점수
    for i in info:
        a, b, c, d, e = i.split()
        arr[tmp[a]][tmp[b]][tmp[c]][tmp[d]].append(int(e))
    for a in range(3): 
        for b in range(2): 
            for c in range(2): 
                for d in range(2): 
                    arr[a][b][c][d].sort()
    for q in query:
        a, _, b, _, c, _, d, e = q.split()
        cnt = 0
        if a == "-": t1 = [0, 1, 2]
        else: t1 = [tmp[a]]
        if b == "-": t2 = [0, 1]
        else: t2 = [tmp[b]]
        if c == "-": t3 = [0, 1]
        else: t3 = [tmp[c]]
        if d == "-": t4 = [0, 1]
        else: t4 = [tmp[d]]
        for r1 in t1:
            for r2 in t2:
                for r3 in t3:
                    for r4 in t4:
                        cnt += (len(arr[r1][r2][r3][r4]) - bisect_left(arr[r1][r2][r3][r4], int(e)))
        answer.append(cnt)
                        
    return answer