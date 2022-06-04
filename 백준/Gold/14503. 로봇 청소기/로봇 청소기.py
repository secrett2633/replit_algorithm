import sys
input = sys.stdin.readline
n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = 1
arr[r][c] = 2
def solve(x, y, direction, ns):
  global res
  if direction == 0:
    if arr[x][y - 1] == 0:      
      arr[x][y - 1] = 2
      res += 1
      return (x, y - 1, 3, 0)
    else:
      return (x, y, 3, ns + 1)

  elif direction == 1:
    if arr[x - 1][y] == 0:      
      arr[x - 1][y] = 2
      res += 1
      return (x - 1, y, 0, 0)
    else:
      return (x, y, 0, ns + 1)

  elif direction == 2:
    if arr[x][y + 1] == 0:      
      arr[x][y + 1] = 2
      res += 1
      return (x, y + 1, 1, 0)
    else:
      return (x, y, 1, ns + 1)

  else:
    if arr[x + 1][y] == 0:      
      arr[x + 1][y] = 2
      res += 1
      return (x + 1, y, 2, 0)
    else:
      return (x, y, 2, ns + 1)
      
s = 0
while True:
  r, c, d, s = solve(r, c, d, s)
  if s == 4:
    s = 0
    if d == 0:
      if arr[r + 1][c] == 1:
        break
      else:
        if arr[r + 1][c] != 2:
          res += 1
        arr[r + 1][c] = 2
        r += 1        
        
    elif d == 1:
      if arr[r][c - 1] == 1:
        break
      else:
        if arr[r][c - 1] != 2:
          res += 1
        arr[r][c - 1] = 2
        c -= 1        

    elif d == 2:
      if arr[r - 1][c] == 1:
        break
      else:
        if arr[r - 1][c] != 2:
          res += 1
        arr[r - 1][c] = 2
        r -= 1        

    else:
      if arr[r][c + 1] == 1:
        break
      else:
        if arr[r][c + 1] != 2:
          res += 1
        arr[r][c + 1] = 2
        c += 1        
  
print(res)