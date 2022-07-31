import sys
from collections import deque
import copy
import math
input = sys.stdin.readline
from collections import Counter
def solve():
    tmp = 0
    for j in range(len(s)):
        a = [i for i in s[j] if i != 0]
        a = Counter(a).most_common()
        a.sort(key = lambda x : (x[1], x[0]))
        s[j] = []
        for fi, se in a:
            s[j].append(fi)
            s[j].append(se)
        if tmp < len(a) * 2: tmp = len(a) * 2
    for j in range(len(s)):
        for k in range(tmp - len(s[j])):
            s[j].append(0)
        s[j] = s[j][:100]
r, c, k = map(int, input().split())
s = [list(map(int, input().split())) for i in range(3)]
for i in range(101):
    try: 
      if s[r - 1][c - 1] == k: print(i); break
    except: pass
    if len(s) < len(s[0]): s = list(zip(*s)); solve(); s = list(zip(*s))
    else: solve()
else: print(-1)