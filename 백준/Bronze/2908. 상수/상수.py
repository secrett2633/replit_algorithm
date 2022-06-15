a, b = list(map(str, input().split()))
temp1 = a[0]
temp2 = a[2]
a = temp2 + a[1] + temp1

temp1 = b[0]
temp2 = b[2]
b = temp2 + b[1] + temp1

if int(a) > int(b):
  print(a)
else:
  print(b)