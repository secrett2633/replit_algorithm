import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
m, s, g = map(int, input().split())
a, b = map(float, input().split())
l, r = map(int, input().split())
if l / a + m / g > r / b + m / s:
  print("latmask")
else:
  print("friskus")