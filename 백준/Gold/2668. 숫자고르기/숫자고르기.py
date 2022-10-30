import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]
answer = []
for i in range(n):
    if not i in answer:
        now = i
        visited = [False] * n
        a = set()
        b = set()
        while now not in a:
            a.add(now)            
            now = arr[now] - 1
            b.add(now)
        if sorted(list(a)) == sorted(list(b)):
            answer.extend(a)
print(len(answer))
answer.sort()
for i in answer:
    print(i + 1)