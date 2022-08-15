import sys
input = sys.stdin.readline
while True:
  try: 
    n, *arr = list(map(int, input().split()))
  except: 
    break
  if n == 1: print("Jolly")
  else:
    visited = [False] * (n - 1)
    for i in range(n - 1):
      try:
        visited[abs(arr[i] - arr[i + 1]) - 1] = True
      except:
        continue
    if all(visited): print("Jolly")
    else: print("Not jolly")