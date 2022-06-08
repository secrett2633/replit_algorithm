import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
w1 = int(input())
h1 = int(input())
w2 = int(input())
h2 = int(input())
print(2 * (max(w1, w2) + (h1 + h2)) + 4)