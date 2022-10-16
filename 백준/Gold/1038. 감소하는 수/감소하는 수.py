from collections import deque
n = int(input())
visited = []
q = deque(list(range(10)))
while q:
    a = q.pop()
    visited.append(a)
    a = str(a)
    for i in range(int(a[-1])):
        q.append(int(a + str(i)))
visited.sort()
try: print(visited[n])
except: print(-1)