from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
result = []
kill = k - 1
for i in range(n):
  kill %= len(arr)
  result.append(str(arr[kill]))
  del arr[kill]
  kill += (k - 1)

print("<", end = "")
for i in range(len(result) - 1):
  print(result[i] + ", ", end = "")
print(result[-1], end = "")
print(">")