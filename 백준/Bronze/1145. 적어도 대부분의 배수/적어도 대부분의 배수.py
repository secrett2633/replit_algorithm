import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
arr = list(map(int, input().split()))
res = 1
while True:
  temp = 0
  if res % arr[0] == 0: temp += 1
  if res % arr[1] == 0: temp += 1
  if res % arr[2] == 0: temp += 1
  if res % arr[3] == 0: temp += 1
  if res % arr[4] == 0: temp += 1
  if temp >= 3:
    print(res)
    break
  res += 1