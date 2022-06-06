import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n = int(input())
res = (100 - n) / n + 1
res1 = n / (100 - n) + 1
print("%.10f" % res)
print("%.10f" % res1)