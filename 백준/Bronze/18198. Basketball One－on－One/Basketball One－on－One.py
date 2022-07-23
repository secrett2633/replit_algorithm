arr = input().rstrip()
a = 0
b = 0
flag = True
for i in range(len(arr) // 2):
  if arr[i * 2:i * 2 + 2] == "A1":
    a += 1
  elif arr[i * 2:i * 2 + 2] == "A2":
    a += 2
  elif arr[i * 2:i * 2 + 2] == "B1":
    b += 1
  elif arr[i * 2:i * 2 + 2] == "B2":
    b += 2
  if a == b == 10: flag = False
  if flag:
    if a >= 11: print("A"); break
    elif b >= 11: print("B"); break
  else:
    if a > b + 1: print("A"); break
    elif b > a + 1: print("B"); break
  