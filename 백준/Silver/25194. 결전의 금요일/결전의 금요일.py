n = int(input())
a = list(map(int, input().split()))
arr = set([a[0] % 7])
for i in range(1, n):
  for j in list(arr):    
    arr.add((a[i] + j) % 7)
  arr.add(a[i] % 7)
cnt = False
for i in arr:
  if i % 7 == 4:
    cnt = True
if cnt:
  print("YES")
else:
  print("NO")