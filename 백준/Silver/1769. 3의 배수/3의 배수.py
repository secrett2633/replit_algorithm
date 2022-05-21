import sys
input = sys.stdin.readline
x = int(input())
cnt = 0
while x >= 10:
  temp = 0
  for i in list(str(x)):
    temp += int(i)
  cnt += 1
  x = temp
print(cnt)
if x % 3 == 0:
  print("YES")
else:
  print("NO")