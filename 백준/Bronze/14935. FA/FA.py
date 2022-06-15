import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x = int(input())
while True:
  temp = len(str(x)) * int(str(x)[0])
  if temp == x:
    print("FA")
    exit(0)
  x = temp
