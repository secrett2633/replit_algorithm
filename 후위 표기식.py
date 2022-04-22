import sys
from collections import deque
input = sys.stdin.readline
arr = list(input().rstrip())
q = deque(arr)
result = ""
oper = deque()
while q:
  a = q.popleft()
  if a == "+" or a == "-":
    while oper and oper[-1] != "(":
      result += oper.pop()
    oper.append(a)
  elif a == "*" or a == "/":
    while oper and (oper[-1] == "*" or oper[-1] == "/"):
      result += oper.pop()
    oper.append(a)
  elif a == "(":
    oper.append(a)
  elif a == ")":
    while oper and oper[-1] != "(":
      result += oper.pop()
    oper.pop()
  else:
    result += a
while oper:
  result += oper.pop()
print(result)