import sys
input = sys.stdin.readline
n = int(input())
s = input().rstrip()
cache = {"U":0, "D":1, "L":2, "R":3}
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
nx = 0
ny = 0
arr = [["."] * n for _ in range(n)]
for i in s:
  if (0 <= nx + dx[cache[i]] < n) and (0 <= ny + dy[cache[i]] < n):
    if arr[nx][ny] == ".":
      if i == "D" or i == "U": arr[nx][ny] = "|"
      else: arr[nx][ny] = "-"
    elif arr[nx][ny] == "|" and (i == "L" or i == "R"): arr[nx][ny] = "+"
    elif arr[nx][ny] == "-" and (i == "D" or i == "U"): arr[nx][ny] = "+"
    nx, ny = nx + dx[cache[i]], ny + dy[cache[i]]
  else: continue
  if arr[nx][ny] == ".":
    if i == "D" or i == "U": arr[nx][ny] = "|"
    else: arr[nx][ny] = "-"
  elif arr[nx][ny] == "|" and (i == "L" or i == "R"): arr[nx][ny] = "+"
  elif arr[nx][ny] == "-" and (i == "D" or i == "U"): arr[nx][ny] = "+"
for i in arr:
  print("".join(map(str, i)))