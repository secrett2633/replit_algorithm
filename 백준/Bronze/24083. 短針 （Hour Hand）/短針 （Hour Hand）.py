import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
b = int(input())
res = (a + b) % 12
print(res if res != 0 else 12)