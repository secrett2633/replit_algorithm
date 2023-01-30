import sys
from collections import deque
import heapq
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
s = res = 0
e = 1
cnt = arr[0]
while True:
    if cnt < m and e < n: cnt += arr[e]; e += 1
    elif cnt < m: break
    elif cnt > m: cnt -= arr[s]; s += 1
    else: res += 1; cnt -= arr[s]; s += 1
print(res)   