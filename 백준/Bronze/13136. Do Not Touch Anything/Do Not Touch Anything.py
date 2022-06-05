import sys
import math
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
n, m, k = map(int, input().rstrip().split())
print(math.ceil(n / k) * math.ceil(m / k))