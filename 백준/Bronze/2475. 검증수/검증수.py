a = map(int, input().split())
cnt = 0
for i in a:
  cnt += i * i
print(cnt % 10)