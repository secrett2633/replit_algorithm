import sys
input = sys.stdin.readline
n, r, c = map(int, input().split())
graph = (2 ** n) * (2 ** n) 
start = 0
end = graph - 1
while graph > 4:
  if r // (graph ** (0.5) // 2) == 0:
    if c // (graph ** (0.5) // 2) == 0: #1사분면
      end = (end + 1) // 4 - 1
    else: #2사분면
      start += (graph // 4)
      end = start + (graph // 4) - 1
  elif r // (graph ** (0.5) // 2) == 1:
    if c // (graph ** (0.5) // 2) == 0: #3사분면
      start += (graph // 4 * 2) 
      end = start + (graph // 4) - 1
    else: #4사분면
      start += (graph // 4 * 3) 
      end = start + (graph // 4) - 1
  r %= (graph ** (0.5) // 2)
  c %= (graph ** (0.5) // 2)
  graph = graph // 4
print(int(start + r * 2 + c))