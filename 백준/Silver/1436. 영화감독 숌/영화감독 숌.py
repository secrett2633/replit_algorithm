n = int(input())
cnt = 0
m = 0
while True:
  cnt += 1
  if "666" in str(cnt):
    m += 1
  if m == n:
    break
print(cnt)