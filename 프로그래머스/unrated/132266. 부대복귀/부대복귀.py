def solution(n, roads, sources, destination):
    answer = []
    graph = {i : [] for i in range(n + 1)}
    for a, b in roads:
        graph[a].append(b)
        graph[b].append(a)
    from collections import deque
    visited = [-1] * (n + 1)
    q = deque([[0, destination]])
    while q:
        cnt, now = q.popleft()
        if visited[now] != -1: continue
        visited[now] = cnt
        for k in graph[now]:
            q.append([cnt + 1, k])
    return [visited[i] for i in sources]