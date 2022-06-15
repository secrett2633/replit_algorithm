import sys
input = sys.stdin.readline
arr = []
res = 0
for i in range(8):
  arr.append((int(input()), i + 1))
arr.sort(reverse = True)
arr = arr[:5]
result = []
for a, b in arr:
  res += a
  result.append(b)
print(res)
result.sort()
print(" ".join(map(str, result)))