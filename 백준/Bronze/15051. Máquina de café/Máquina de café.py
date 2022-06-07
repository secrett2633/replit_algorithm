import sys
#import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
a1 = int(input())
a2 = int(input())
a3 = int(input())
print(min(a2 * 2 + a3 * 4, a1 * 2 + a3 * 2, a2 * 2 + a1 * 4))
