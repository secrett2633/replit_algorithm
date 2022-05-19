import sys
input = sys.stdin.readline
n, k = map(int, input().split())
arr = [[1], [1, 1]]
for i in range(1, n):
  temp = [1]
  for j in range(len(arr[i]) - 1):
    temp.append(arr[i][j] + arr[i][j + 1])
  temp.append(1)
  arr.append(temp)
print(arr[n - 1][k - 1])