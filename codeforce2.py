import sys
import string
import itertools
input = sys.stdin.readline
alpha = list(string.ascii_lowercase)
it = list(itertools.permutations(alpha, 2))
for _ in range(int(input())):
  s = list(input().rstrip())
  result = it.index((s[0], s[1]))
  print(result + 1)
  