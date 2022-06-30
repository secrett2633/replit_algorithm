import sys
input = sys.stdin.readline
k, s, n = input().rstrip().split()
q = [input().rstrip() for _ in range(int(n))]
y1 = ord(k[0]) - 65
x1 = 8 - int(k[1])
y2 = ord(s[0]) - 65
x2 = 8 - int(s[1])
for i in q:
  if i == "R":
    if y1 + 1 == 8:
      continue
    if y1 + 1 == y2 and x1 == x2:
      if y2 + 1 == 8:
        continue
      else:
        y1 += 1; y2 += 1
    else:
      y1 += 1

  elif i == "L":
    if y1 - 1 == -1:
      continue
    if y1 - 1 == y2 and x1 == x2:
      if y2 - 1 == -1:
        continue
      else:
        y1 -= 1; y2 -= 1
    else:
      y1 -= 1

  elif i == "B":
    if x1 + 1 == 8:
      continue
    if x1 + 1 == x2 and y1 == y2:
      if x2 + 1 == 8:
        continue
      else:
        x1 += 1; x2 += 1
    else:
      x1 += 1

  elif i == "T":
    if x1 - 1 == -1:
      continue
    if x1 - 1 == x2 and y1 == y2:
      if x2 - 1 == -1:
        continue
      else:
        x1 -= 1; x2 -= 1
    else:
      x1 -= 1

  elif i == "RT":
    if x1 - 1 == -1 or y1 + 1 == 8:
      continue
    if x1 - 1 == x2 and y1 + 1 == y2:
      if x2 - 1 == -1 or y2 + 1 == 8:
        continue
      else:
        x1 -= 1; x2 -= 1; y1 += 1; y2 += 1
    else:
      x1 -= 1; y1 += 1

  elif i == "LT":
    if x1 - 1 == -1 or y1 - 1 == -1:
      continue
    if x1 - 1 == x2 and y1 - 1 == y2:
      if x2 - 1 == -1 or y2 - 1 == -1:
        continue
      else:
        x1 -= 1; x2 -= 1; y1 -= 1; y2 -= 1
    else:
      x1 -= 1; y1 -= 1

  elif i == "RB":
    if x1 + 1 == 8 or y1 + 1 == 8:
      continue
    if x1 + 1 == x2 and y1 + 1 == y2:
      if x2 + 1 == 8 or y2 + 1 == 8:
        continue
      else:
        x1 += 1; x2 += 1; y1 += 1; y2 += 1
    else:
      x1 += 1; y1 += 1

  elif i == "LB":
    if x1 + 1 == 8 or y1 - 1 == -1:
      continue
    if x1 + 1 == x2 and y1 - 1 == y2:
      if x2 + 1 == 8 or y2 - 1 == -1:
        continue
      else:
        x1 += 1; x2 += 1; y1 -= 1; y2 -= 1
    else:
      x1 += 1; y1 -= 1
print(chr(y1 + 65) + str(8 - x1))
print(chr(y2 + 65) + str(8 - x2))