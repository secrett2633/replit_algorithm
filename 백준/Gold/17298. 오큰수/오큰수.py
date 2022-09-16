import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [-1] * n
q = deque([0])
for i in range(1, n):
    while q and arr[i] > arr[q[-1]]:
        res[q.pop()] = arr[i]
    q.append(i)
print(*res)