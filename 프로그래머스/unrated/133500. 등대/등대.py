def solution(n, lighthouse):
    import sys
    sys.setrecursionlimit (10 ** 5)
    graph = {i : [] for i in range(1, n + 1)}
    for a, b in lighthouse:
        graph[a].append(b)
        graph[b].append(a)
    def solve(now, visited):
        a = [i for i in graph[now] if not visited[i]]
        notvisit = 0
        visit = 1
        if not a: return notvisit, visit
        visited[now] = 1
        for i in a:
            n, nn = solve(i, visited)
            visit += min(n, nn)
            notvisit += nn
        return notvisit, visit
    return min(solve(1, [0] * (n + 1)))