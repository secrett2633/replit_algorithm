import sys
import heapq
input = sys.stdin.readline
n = int(input())
arr = [int(input())]
res = 0
for _ in range(n - 1):
    now = int(input())
    i = 0
    while arr and arr[0] <= now:
        heapq.heappop(arr)
    res += len(arr)
    heapq.heappush(arr, now)
print(res)