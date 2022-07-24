for _ in range(int(input())):
  a, b = input().split()
  if a == b or a == b[::-1]: print("OK")
  else: print("ERROR")