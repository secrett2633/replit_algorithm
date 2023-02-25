import sys
from collections import deque
input = sys.stdin.readline
a = input().rstrip()
b = input().rstrip()
q = deque([a])
while q:
    s = q.popleft()
    if s == b: print(1); break
    if len(s) >= len(b): continue
    if not (s in b or s[::-1] in b): continue
    q.append(s + "A")
    q.append("B" + s[::-1])
else: print(0)