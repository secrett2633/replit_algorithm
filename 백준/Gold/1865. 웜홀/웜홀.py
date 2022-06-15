import sys
input = sys.stdin.readline
def bf(start):
    dist = [int(1e9)] * (n+1)
    dist[start]=0
    for i in range(n):
        for edge in edges:
            cur = edge[0] 
            next_node = edge[1]
            cost = edge[2] 
            if dist[next_node] > cost + dist[cur]:
                dist[next_node] = cost + dist[cur]
                if i == n - 1:
                    return True

    return False
for _ in range(int(input())):
    # 지점수, 도로수, 웜홀수
    n, m, w = map(int, input().split())
    edges = []
    for _ in range(m):
        s, e, t = map(int, input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s, e, t = map(int, input().split())
        edges.append([s, e, -t])
    key = bf(1)
    if key:
        print("YES")
    else:
        print("NO")