import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = []

for i in range(n):
  arr.append(input().strip())
for i in range(m):
  N = input().strip()
  if N.isdigit():
    N = int(N)
    print(arr[N - 1])
  else:
    print(arr.index(N) + 1)