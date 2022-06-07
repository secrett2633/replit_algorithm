import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())
if p1 + p2 > s1 + s2:
  print("Persepolis")
elif p1 + p2 < s1 + s2:
  print("Esteghlal")
elif s1 > p2:
  print("Esteghlal")
elif s1 < p2:
  print("Persepolis")
else:
  print("Penalty")