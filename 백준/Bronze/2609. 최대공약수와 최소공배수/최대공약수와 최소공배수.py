import sys
input = sys.stdin.readline

a, b = map(int, input().split())
arr = []
for i in range(1, min(a, b) + 1):
  if min(a, b) % i == 0:
    arr.append(i)
arr.sort(reverse = True)

for i in arr:
  if max(a, b) % i == 0:
    print(i)
    break

for i in range(1, 10001):
  if (max(a, b) * i) % min(a, b) == 0:
    print(max(a, b) * i)
    break