import sys
input = sys.stdin.readline
arr = [0]
for i in range(1, 5001):
  if sorted(list(str(i))) == sorted(list(set(list(str(i))))): 
    arr.append(arr[-1] + 1)
  else:
    arr.append(arr[-1])
while True:
  try:
    n, m = map(int, input().split())
    print(arr[m] - arr[n - 1])
  except:
    break
    