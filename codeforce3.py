import sys
input = sys.stdin.readline
for _ in range(int(input())):
  s = input().rstrip()
  t = input().rstrip()
  result = [s]
  for i in range(50):
    s = s.replace('a', t, 1)
    if s not in result:
      result.append(s)
  print(len(result) if len(result) <= 50 else "-1")
  
  