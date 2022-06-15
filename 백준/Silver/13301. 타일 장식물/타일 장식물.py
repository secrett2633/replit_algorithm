import sys
input = sys.stdin.readline
n = int(input())
x = 1
y = 1
for i in range(1, n):
  if x >= y:
    y += x
  else:
    x += y
print((x + y) * 2)