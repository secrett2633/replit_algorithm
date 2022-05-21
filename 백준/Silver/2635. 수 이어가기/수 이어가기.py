import sys
input = sys.stdin.readline
n = int(input())
result = []
for i in range(n, -1, -1):
  temp = [n, n - i]
  while temp[-2] - temp[-1] >= 0:
    temp.append(temp[-2] - temp[-1])
  if len(result) < len(temp):
    result = temp[::]
print(len(result))
print(" ".join(map(str, result)))
      