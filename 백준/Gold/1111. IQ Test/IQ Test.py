import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
if n == 1: print("A"); exit(0)
elif n == 2:
  if arr[0] == arr[1]: print(arr[0]); exit(0)
  else: print("A"); exit(0)
if (arr[0] - arr[1]) != 0: a = (arr[1] - arr[2]) // (arr[0] - arr[1])
else: a = 0
b = arr[1] - arr[0] * a
for i in range(1, n):
  if arr[i - 1] * a + b != arr[i]: print("B"); exit(0)
print(arr[-1] * a + b)