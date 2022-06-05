import sys
#from math import sqrt
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
s, t, d = map(int, input().split())
res = d // (s * 2)
print(res * t)