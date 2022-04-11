import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
  arr.append(list(map(int, input().split())))
result = []
for i in range(n):
  cnt = 1
  for j in range(n):
    if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
      cnt += 1
  result.append(str(cnt))
print(" ".join(result))