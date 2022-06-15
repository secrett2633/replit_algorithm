import sys
input = sys.stdin.readline
res = 0
board = [[False] * 7 for _ in range(7)]
#print(ord("A" - 64))
s = input().rstrip()
board[ord(s[0]) - 64][int(s[1])] = True
prev = [ord(s[0]) - 64, int(s[1])]
first = [ord(s[0]) - 64, int(s[1])]
flag = True
for i in range(35):
  s = input().rstrip()
  if (abs((ord(s[0]) - 64) - prev[0]) == 1 and abs(int(s[1]) - prev[1]) == 2) or (abs((ord(s[0]) - 64) - prev[0]) == 2 and abs(int(s[1]) - prev[1]) == 1):
    if not board[ord(s[0]) - 64][int(s[1])]:
      prev = [ord(s[0]) - 64, int(s[1])]
      board[ord(s[0]) - 64][int(s[1])] = True
      continue
  flag = False
if flag and ((abs(first[0] - prev[0]) == 1 and abs(first[1] - prev[1]) == 2) or (abs(first[0] - prev[0]) == 2 and abs(first[1] - prev[1]) == 1)):
  print("Valid")
else:
  print("Invalid")