import sys
input = sys.stdin.readline
l, c = map(int, input().split())
word = sorted(list(input().split()))
result = []
vowel = ["a", "e", "i", "o", "u"]
def solve(now, n, vo, no):
  if len(now) == l:
    if vo >= 1 and no >= 2:
      result.append(now)
    return
  for i in range(n, c):
    if word[i] in vowel:
      solve(now + word[i], i + 1, vo + 1, no)
    else:
      solve(now + word[i], i + 1, vo, no + 1)

solve("", 0, 0, 0)
print("\n".join(result))