import sys
from itertools import product
import math
input = sys.stdin.readline
n, m = map(int, input().split(":"))
print(str(n // math.gcd(n, m)) + ":" + str(m // math.gcd(n, m)))