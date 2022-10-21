import sys
input = sys.stdin.readline
n = int(input())
s = list(input().rstrip())
for i in range(n - 1):
  if s[n - i - 2] != s[n - i - 1]:
      if s[n - i - 2] == "A" and s[n - i - 1] == "G": s[n - i - 2] = "C"
      elif s[n - i - 2] == "A" and s[n - i - 1] == "T": s[n - i - 2] = "G"
      elif s[n - i - 2] == "G" and s[n - i - 1] == "A": s[n - i - 2] = "C"
      elif s[n - i - 2] == "G" and s[n - i - 1] == "C": s[n - i - 2] = "T"
      elif s[n - i - 2] == "G" and s[n - i - 1] == "T": s[n - i - 2] = "A"
      elif s[n - i - 2] == "C" and s[n - i - 1] == "A": s[n - i - 2] = "A"
      elif s[n - i - 2] == "C" and s[n - i - 1] == "G": s[n - i - 2] = "T"
      elif s[n - i - 2] == "C" and s[n - i - 1] == "T": s[n - i - 2] = "G"
      elif s[n - i - 2] == "T" and s[n - i - 1] == "A": s[n - i - 2] = "G"
      elif s[n - i - 2] == "T" and s[n - i - 1] == "G": s[n - i - 2] = "A"
      elif s[n - i - 2] == "T" and s[n - i - 1] == "C": s[n - i - 2] = "G"
print(s[0])