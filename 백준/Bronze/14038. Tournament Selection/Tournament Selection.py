import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
cnt = 0
for i in range(6):
  s = input().rstrip()
  if s == "W":
    cnt += 1

if cnt >= 5:
  print(1)
elif cnt >= 3:
  print(2)
elif cnt >= 1:
  print(3)
else:
  print(-1)