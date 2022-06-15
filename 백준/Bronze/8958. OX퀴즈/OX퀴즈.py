t = int(input())
for i in range(t):
  a = input()
  cnt = 0
  result = 0
  for i in range(len(a)):
    if a[i] == "O":
      cnt += 1
      result += cnt
    else:
      cnt = 0
  print(result)