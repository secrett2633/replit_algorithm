import sys
input = sys.stdin.readline
n = int(input())
arr = [1] * 988
for i in range(123, 988):
  i = str(i)
  if i[0] == i[1] or i[1] == i[2] or i[0] == i[2]:
    arr[int(i)] = 0
  if i[0] == '0' or i[1] == '0' or i[2] == '0':
    arr[int(i)] = 0
for i in range(n):
  a, b, c = map(int, input().split())  
  for j in range(123, 988):    
    ns, nb = 0, 0
    if arr[j] == 0: continue
    for k in range(3):
      for l in range(3):
        if str(j)[k] == str(a)[l]:
          if k == l:
            ns += 1
          else:
            nb += 1
    if arr[j] == 1 and ns == b and nb == c:
      arr[j] = 1
    else:
      arr[j] = 0
print(sum(arr[123:988]))