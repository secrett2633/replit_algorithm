a = []
for i in range(1, 10000):
  temp = str(i)
  lenth = len(temp)
  result = i
  for j in range(lenth):
    result += int(temp[j])
  a.append(result)
b = set([i for i in range(1, 10000)])
a = set(a)
c = b.difference(a)
c = list(c)
c.sort()
for i in c:
  print(i)