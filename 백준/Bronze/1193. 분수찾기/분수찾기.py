import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x = int(input())
now = 0
t = 1
while True:
  now += t
  if now >= x:
    x1 = t - (now - x)
    y1 = now - x + 1
    if t % 2 == 0:
      print("%d/%d" % (x1, y1))
      break
    else:     
      print("%d/%d" % (y1, x1))
      break
  t += 1