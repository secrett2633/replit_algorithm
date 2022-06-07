import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
b = int(input())
res = b * 5 - 400
print(res)
if res < 100:
  print(1)
elif res > 100:
  print(-1)
else:
  print(0)