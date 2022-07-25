for i in range(int(input())):
  a = 0
  b = 0
  for _ in range(int(input())):
    c, d = input().split()
    if c == "R" and d == "P": b += 1
    elif c == "R" and d == "S": a += 1
    elif c == "P" and d == "R": a += 1
    elif c == "P" and d == "S": b += 1
    elif c == "S" and d == "R": b += 1
    elif c == "S" and d == "P": a += 1
  if a > b: print("Player 1")
  elif a < b: print("Player 2")
  else: print("TIE")