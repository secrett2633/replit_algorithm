import sys
input = sys.stdin.readline
from collections import Counter
s = ""
for _ in range(50):
  try:
    s += input().rstrip()
  except:
    break
s = s.replace(" ", "")
a = Counter(s).most_common()
res = a[0][1]
ans = []
for i in a:
  if i[1] != res: break
  ans.append(i[0])
ans.sort()
print("".join(ans))