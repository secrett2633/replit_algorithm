import sys
import math
input = sys.stdin.readline
n = int(input())
div = 2
while n > 1:
  while n % div == 0:
    print(div)
    n = n // div
  div += 1