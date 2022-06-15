n = int(input())
arr = []
for i in range(n):
  arr.append(input())
arr = set(arr)
arr = list(arr)
arr.sort()
arr.sort(key = lambda x:len(x))
for i in arr:
  print(i)