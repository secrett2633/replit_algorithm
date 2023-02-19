def solution(n, paths, gates, summits):
    from collections import deque
    answer = [int(1e9), int(1e9)]
    graph = {i : [] for i in range(1, n + 1)}
    for i, j, w in paths:
        graph[i].append([j, w])
        graph[j].append([i, w])
    summit = [False] * (n + 1)
    for i in summits:
        summit[i] = True
    gate = [int(1e9)] * (n + 1)
    for i in gates:
        gate[i] = -1
    q = deque()
    for start in set(gates):
        q.append([start, 0])
    visited = [int(1e9)] * (n + 1)
    while q:
        now, cnt = q.popleft()
        if summit[now]: 
            if answer[1] > cnt: answer = [now, cnt]
            elif answer[1] == cnt: answer[0] = min(answer[0], now)
            continue
        elif visited[now] <= cnt: continue
        elif cnt > answer[1]: continue
        visited[now] = cnt
        for i, c in graph[now]:
            q.append([i, max(cnt, c)])
    return answer