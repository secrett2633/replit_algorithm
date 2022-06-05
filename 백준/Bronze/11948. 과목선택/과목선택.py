import sys
#from collections import Counter
#from string import ascii_lowercase
#alphabet_list = ascii_lowercase
input = sys.stdin.readline
res = []
for i in range(4):
  res.append(int(input()))
res.sort(reverse = True)
result = sum(res[:3])
res = []
for i in range(2):
  res.append(int(input()))
res.sort(reverse = True)
print(result + res[0])