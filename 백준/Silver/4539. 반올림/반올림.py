import sys
input = sys.stdin.readline
def rnd(num, i):
  if int(str(num)[-i]) >= 5:
    num += 10 ** i
  num -= int(str(num)[-i]) * (10 ** (i - 1)) 
  return num
for _ in range(int(input())):
  x = int(input())
  for i in range(1, len(str(x))):
    x = rnd(x, i)
  print(x)