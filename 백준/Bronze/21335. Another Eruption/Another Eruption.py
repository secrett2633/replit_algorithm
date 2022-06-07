import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a = int(input())
n = (a / math.pi) ** (0.5) 
print(n * 2 * math.pi)