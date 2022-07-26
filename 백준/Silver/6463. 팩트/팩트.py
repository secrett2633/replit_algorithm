import sys
input = sys.stdin.readline
arr = [1]
for i in range(1, 10001):
  arr.append(arr[i - 1] * i)
while True:
  try:
    n = int(input())
  except:
    break
  for j in str(arr[n])[::-1]:
    if j != "0": cnt = int(j); break
  print((5 - len(str(n))) * " " + str(n) + " -> " + str(cnt))