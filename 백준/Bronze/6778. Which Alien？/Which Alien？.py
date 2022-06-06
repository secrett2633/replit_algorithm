import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
b = int(input())
if a >= 3 and b <= 4:
  print("TroyMartian")
if a <= 6 and b >= 2:
  print("VladSaturnian")
if a <= 2 and b <= 3:
  print("GraemeMercurian")