import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
w, h = map(int, input().split())
res = (w * w + h * h) ** 0.5
print(w + h - res)