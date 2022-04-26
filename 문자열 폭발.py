import sys
input = sys.stdin.readline
s = list(input().rstrip())
ex = list(input().rstrip())
stack = []
for i in range(len(s)):
  stack.append(s[i])
  if len(stack) >= len(ex):
    if stack[-len(ex):] == ex:
      for j in range(len(ex)):
        stack.pop()
print("".join(map(str, stack)) if len(stack) != 0 else "FRULA")