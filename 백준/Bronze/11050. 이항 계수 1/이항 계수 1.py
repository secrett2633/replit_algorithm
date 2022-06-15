from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
result = 1
result1 = 1
for i in range(n, n - k , -1):
  result *= i

for i in range(k, 0, -1):
  result1 *= i

print(int(result / result1))