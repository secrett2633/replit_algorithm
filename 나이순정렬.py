import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(input().split()))
for i in arr:
  i[0] = int(i[0])
arr.sort(key = lambda x:x[0])
for i in arr:
  print(str(i[0]) + " " + i[1])