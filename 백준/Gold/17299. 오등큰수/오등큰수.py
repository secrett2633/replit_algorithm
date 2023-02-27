import sys
from collections import deque
import heapq
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
cnt = {}
for i in arr:
    try: cnt[i] += 1
    except: cnt[i] = 1
arr1 = list(map(lambda x: cnt[x], arr))
res = []
q = deque()
for i in range(n - 1, -1, -1):
    tmp = -1
    while q:
        if q[-1][0] > arr1[i]: tmp = arr[q[-1][1]]; break
        else: q.pop()
    res.append(tmp)
    q.append((arr1[i], i))
print(*res[::-1])