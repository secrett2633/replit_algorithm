x, y = input().split()
x = int(x)
y = int(y)
if x > 1:
      y += 31
if x > 2:
      y += 28
if x > 3:
      y += 31
if x > 4:
      y += 30
if x > 5:
      y += 31
if x > 6:
      y += 30
if x > 7:
      y += 31
if x > 8:
      y += 31
if x > 9:
      y += 30
if x > 10:
      y += 31
if x > 11:
      y += 30
y = y % 7
if y == 0:
      print("SUN")
elif y == 1:
      print("MON")
elif y == 2:
      print("TUE")
elif y == 3:
      print("WED")
elif y == 4:
      print("THU")
elif y == 5:
      print("FRI")
else:
      print("SAT")