def solution(a, edges):
    import sys
    sys.setrecursionlimit(10**7)
    if sum(a) != 0: return -1
    graph = {i:[] for i in range(len(a))}
    for i, j in edges:
        graph[i].append(j)
        graph[j].append(i)
    visited = [False] * len(a)
    def dfs(now, cnt):
        visited[now] = True
        cnt11 = 0
        nodes = [x for x in graph[now] if not visited[x]]
        for node in nodes:
            cnt1, nodev = dfs(node, cnt)  
            a[node] = 0
            a[now] += nodev
            cnt11 += abs(nodev) + cnt1
        return cnt11, a[now]
    return dfs(0, 0)[0]