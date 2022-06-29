import sys
input = sys.stdin.readline

a = "QWERTYUIOP[]\\"
b = "ASDFGHJKL;'"
c = "ZXCVBNM,./"
d = "QAZ`"
e = "`1234567890-="

while True:
  res = ""
  s = input().rstrip()
  if s == "": break
  for i in s:
    if i in d: res += i
    elif i in a: res += a[a.index(i) - 1]
    elif i in b: res += b[b.index(i) - 1]
    elif i in c: res += c[c.index(i) - 1]
    elif i in e: res += e[e.index(i) - 1]  
    else: res += i
  print(res)
      