import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = dict()
for i in range(n):
  a, b = input().split()
  arr[a] = b
for i in range(m):
  print(arr[input().strip()])