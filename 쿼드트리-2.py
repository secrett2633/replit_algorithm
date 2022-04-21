N = int(input())
graph = []
for _ in range(N):
    graph.append(input())
def recursive(arr):
  result = ""
  arr1 = [row[0:len(arr) // 2] for row in arr[0:len(arr) // 2]]
  arr2 = [row[len(arr) // 2:] for row in arr[0:len(arr) // 2]]
  arr3 = [row[0:len(arr) // 2] for row in arr[len(arr) // 2:]]
  arr4 = [row[len(arr) // 2:] for row in arr[len(arr) // 2:]]
  #1
  cnt = True
  cnt1 = True
  for i in range(len(arr1)):
    for j in range(len(arr1)):
      if arr1[i][j] == "1":
        cnt = False
      else:
        cnt1 = False
  if cnt:
    result += "(0"
  elif cnt1:
    result += "(1"
  else:
    result += "(" + recursive(arr1)
  #2
  cnt = True
  cnt1 = True
  for i in range(len(arr2)):
    for j in range(len(arr2)):
      if arr2[i][j] == "1":
        cnt = False
      else:
        cnt1 = False
  if cnt:
    result += "0"
  elif cnt1:
    result += "1"
  else:
    result += recursive(arr2)
  #3
  cnt = True
  cnt1 = True
  for i in range(len(arr3)):
    for j in range(len(arr3)):
      if arr3[i][j] == "1":
        cnt = False
      else:
        cnt1 = False
  if cnt:
    result += "0"
  elif cnt1:
    result += "1"
  else:
    result += recursive(arr3)
  #4
  cnt = True
  cnt1 = True
  for i in range(len(arr4)):
    for j in range(len(arr4)):
      if arr4[i][j] == "1":
        cnt = False
      else:
        cnt1 = False
  if cnt:
    result += "0)"
  elif cnt1:
    result += "1)"
  else:
    result += recursive(arr4) + ")"
  return result


cnt = True
cnt1 = True
for i in range(len(graph)):
  for j in range(len(graph)):
    if graph[i][j] == "1":
      cnt = False
    else:
      cnt1 = False
if cnt:
  print("(0)")
elif cnt1:
  print("(1)")
else:
  print(recursive(graph))

  