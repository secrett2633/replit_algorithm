import sys
input = sys.stdin.readline
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse = True)
start = 0
end = arr[0]
while start <= end:
  height = (start + end) // 2
  cnt = 0
  for i in arr:
    if i - height > 0:
      cnt += i - height
  if cnt >= m: # 가능한경우   
    start = height + 1
  else:    
    end = height - 1
print(end)
