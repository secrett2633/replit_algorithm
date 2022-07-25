for _ in range(10000):
  res = 1
  s = input().rstrip()
  if s == "0": break
  for i in s:
    if i == "0": res += 5
    elif i == "1": res += 3
    else: res += 4
  print(res)