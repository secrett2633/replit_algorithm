import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
x, y = map(int, input().split())
r = int(input())
print(x - r, y + r)
print(x + r, y + r)
print(x + r, y - r)
print(x - r, y - r)