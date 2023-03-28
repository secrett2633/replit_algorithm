import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline
n = int(input())
arr = [0] + list(map(int, input().split()))
graph = {i : list(map(int, input().split()))[1:] for i in range(1, n + 1)}
tmp = set(range(1, n + 1))
answer = int(1e9)
for i in range(1, n):
    for a in combinations(range(1, n + 1), i):
        b = list(tmp - set(a))
        visited = [0] * (n + 1)
        q = deque([a[0]])
        while q:
            now = q.popleft()
            if visited[now]: continue
            visited[now] = True
            for x in graph[now]:
                if x in a and not visited[x]: q.append(x)
        if visited != [i in a for i in range(n + 1)]: continue
        visited = [0] * (n + 1)
        q = deque([b[0]])
        while q:
            now = q.popleft()
            if visited[now]: continue
            visited[now] = True
            for x in graph[now]:
                if x in b and not visited[x]: q.append(x)
        if visited != [i in b for i in range(n + 1)]: continue
        answer = min(answer, abs(sum([arr[i] for i in a]) - sum([arr[i] for i in b])))
print(answer if answer != int(1e9) else -1)