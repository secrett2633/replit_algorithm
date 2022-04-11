import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
  n, m = map(int, input().split())
  important = list(map(int, input().split()))
  arr = list(range(len(important)))  
  arr[m] = "target"
  cnt = 0
  while True:
    if important[0] == max(important):
      cnt += 1
      if arr[0] == "target":
        print(cnt)
        break
      else:
        arr.pop(0)
        important.pop(0)
    else:
      important.append(important.pop(0))
      arr.append(arr.pop(0))