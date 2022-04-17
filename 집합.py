import sys
input = sys.stdin.readline
n = int(input())
arr = set()
for i in range(n):
  a = input().strip().split()
  if len(a) == 2:
    a, b = a[0], a[1]
    b = int(b)
    if a == "add":      
      arr.add(b)
    elif a == "remove":
      arr.discard(b)
    elif a == "check":
      if b in arr:
        print("1")
      else:
        print("0")
    elif a == "toggle":
      if b in arr:
        arr.remove(b)
      else:
        arr.add(b)
  else:
    if a[0] == "all":
      arr = set([i for i in range(1, 21)])
    elif a[0] == "empty":
      arr = set()
  