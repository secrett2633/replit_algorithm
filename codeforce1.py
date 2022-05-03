import sys
input = sys.stdin.readline
for _ in range(int(input())):
  x, y = map(int, input().split())
  if y % x > 0 or x > y:
    print("0 0")
  else:
    a = 1
    b = y // x
    print(str(a) + " " + str(b))
    