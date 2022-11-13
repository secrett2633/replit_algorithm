import sys
from collections import deque
import heapq
input = sys.stdin.readline
s = input().rstrip()
t1 = input().rstrip()
t2 = t1[::-1]
q = set()
q.add(t1)
for _ in range(len(t1) - len(s)):
    cache = set()
    while q:
        now = q.pop()
        if now[-1] == "A": cache.add(now[:-1])
        if now[-1] == "B": cache.add(now[:-1][::-1])
    q = cache
if s in q: print(1)
else: print(0)