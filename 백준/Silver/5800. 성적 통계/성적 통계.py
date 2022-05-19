import sys
input = sys.stdin.readline
k = int(input())
for i in range(1, k + 1):
  arr = list(map(int, input().split()))[1:]
  arr.sort()
  a = arr[-1]
  b = arr[0]
  c = 0
  for j in range(len(arr)):
    if j != len(arr) - 1:
      c = max(c, arr[j + 1] - arr[j])
  print("Class " + str(i))
  print("Max " + str(a) + ", Min " + str(b) + ", Largest gap " + str(c))