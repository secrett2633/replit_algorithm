import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, w, h, l = map(int, input().rstrip().split())
print(min(n, (w // l) * (h // l)))