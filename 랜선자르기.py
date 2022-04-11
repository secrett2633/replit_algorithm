import sys
input = sys.stdin.readline

k, n = map(int, input().split())
arr = []
for i in range(k):
  arr.append(int(input()))

def make_line(num):
  cnt = 0
  for j in arr:
    cnt += j // num
  return cnt
  
start = 1
end = max(arr)

while start <= end:  
  middle = (start + end) // 2
  if make_line(middle) >= n:
    start = middle + 1
  else:
    end = middle - 1

print(end)