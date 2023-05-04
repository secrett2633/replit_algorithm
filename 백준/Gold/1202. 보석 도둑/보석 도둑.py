import sys
input = sys.stdin.readline
n, k = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [[int(input()), int(1e10)] for _ in range(k)]
arr = sorted(a + b)
import heapq
q = []
res = 0
for m, v in arr:
    if v == int(1e10):
        if q:
            res -= heapq.heappop(q)
    else:
        heapq.heappush(q, -v)
print(res)