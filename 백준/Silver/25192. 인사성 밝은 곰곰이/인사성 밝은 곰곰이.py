n = int(input())
a = set()
cnt = 0
for i in range(n):
  temp = input().rstrip()
  if temp != "ENTER":
    a.add(temp)
  else:
    cnt += len(a)
    a = set()
print(cnt + len(a))