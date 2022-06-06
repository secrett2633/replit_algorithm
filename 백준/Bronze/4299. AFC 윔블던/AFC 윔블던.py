import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a, b = map(int, input().split())
x = a + b
y = a - b
if x % 2 != 0 or y % 2 != 0 or a < b:
  print(-1)
else:
  print(x // 2, y // 2)