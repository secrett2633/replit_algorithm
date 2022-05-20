a = input().upper()
visited = []
arr = []
for i in range(len(a)):
  if a[i] not in visited:
    cnt = 0
    visited.append(a[i])
    for k in range(len(a)):
      if a[i] == a[k]:
        cnt += 1
    arr.append(cnt)
result = 0
for i in range(len(visited)):
  if max(arr) == arr[i]:
    result += 1
    arr1 = visited[i]
if result > 1:
  print("?")
else:
  print(arr1)