import sys
import heapq
input = sys.stdin.readline
arr = list(map(int, input().split())) + list(map(int, input().split())) + list(map(int, input().split()))
arr = "".join(map(str, arr))
arr = arr.replace("0", "9")
start = arr.find("9")
q = [(0, arr, start)]
dx = {0 : [1, 3], 1: [0, 2, 4], 2: [1, 5], 3 : [0, 4, 6], 4 : [1, 3, 5, 7], 5 : [2, 4, 8], 6 : [3, 7], 7 : [4, 6, 8], 8 : [5, 7]}
visited = {}
while q:
  cnt, arr, now = heapq.heappop(q)
  try:
    if visited[arr]: continue
  except:
    visited[arr] = True
  if arr == "123456789": print(cnt); break
  for nx in dx[now]:
    s1 = list(arr)
    s1[nx], s1[now] = s1[now], s1[nx]
    s1 = "".join(map(str, s1))
    heapq.heappush(q, (cnt + 1, s1, nx))
else: print(-1)