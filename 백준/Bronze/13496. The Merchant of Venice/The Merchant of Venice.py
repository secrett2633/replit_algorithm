for cnt in range(int(input())):
  n, s, d = map(int, input().split())
  res = 0
  for i in range(n):
    a, b = map(int, input().split())
    if s * d >= a: res += b
  print("Data Set " + str(cnt + 1) + ":")
  print(res)
  print()