a = 0
cnt = 0
for i in range(9):
  b = int(input())
  if a < b:
    a = b
    cnt = i
print(a)
cnt += 1
print(cnt)