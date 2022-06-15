import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []
for i in range(n):
  arr.append(input().strip())
arr1 = []
for i in range(m):
  arr1.append(input().strip())
  
arr = set(arr)
arr1 = set(arr1)

arr2 = list(arr & arr1)
arr2.sort()
print(len(arr2))
for i in arr2:
  print(i)