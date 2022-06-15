t = int(input())
for i in range(t):
  a, b = input().split()
  a = int(a)
  for k in range(len(b)):
    for l in range(a):
      print(b[k], end="")
  print("")