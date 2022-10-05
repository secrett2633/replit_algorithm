import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = sorted([list(map(int, input().split())) for _ in range(n)])
q = []
for i in range(n):
    if q and q[0] <= arr[i][0]: heapq.heappop(q); heapq.heappush(q, arr[i][1])
    else: heapq.heappush(q, arr[i][1])
print(len(q))
        