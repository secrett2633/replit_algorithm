def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

def solution(n, paths, gates, summits):
    graph = [[] for i in range(n + 1)]
    distance = [int(1e9)] * (n + 1)
    for a, b, c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
  
    answer = []
    return answer