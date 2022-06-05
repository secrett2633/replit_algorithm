import sys
from collections import Counter
from string import ascii_lowercase
alphabet_list = ascii_lowercase
input = sys.stdin.readline
res = [0] * 26
s = list(input().rstrip())
a = Counter(s)
for i in range(26):
  res[i] += a[alphabet_list[i]]
print(*res)