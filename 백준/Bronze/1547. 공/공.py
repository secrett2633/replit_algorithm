a = {1:1, 2:0, 3:0}
for _ in range(int(input())):
  i, j = map(int, input().split())
  a[i], a[j] = a[j], a[i]
for i in range(1, 4):
  if a[i] == 1: print(i)