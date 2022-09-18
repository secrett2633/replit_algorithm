import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
res = [0] * n
q = deque([n - 1])
for i in range(n - 2, -1, -1):
    while q and arr[i] > arr[q[-1]]:
        res[q.pop()] = i + 1
    q.append(i)
print(*res)