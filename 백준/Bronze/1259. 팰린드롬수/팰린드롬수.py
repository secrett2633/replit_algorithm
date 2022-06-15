while True:
  n = input()
  if n == "0":
    break
  temp = ""
  for i in range(len(n) - 1, -1, -1):
    temp += n[i]
  if temp == n:
    print("yes")
  else:
    print("no")