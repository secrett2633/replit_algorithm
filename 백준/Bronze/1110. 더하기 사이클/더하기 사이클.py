A = int(input())
def cycle(num):
  num = str(num)
  if len(num) == 2:
    a = str(int(num[0]) + int(num[1]))
    a = a[-1]
    b = num[1]
    c = b + str(a)
  else:
    a = int(num[0])
    b = num[0]
    c = b + str(a)
  return c

result = cycle(A)
count = 1
while True:
  if int(result) == A:
    break
  else:
    result = cycle(result)
    count += 1
  
print(count)