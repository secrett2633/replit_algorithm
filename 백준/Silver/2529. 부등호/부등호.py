def findMax(depth, result):
      global find
      if depth == k + 1:
            find = 1
            return
      for i in range(9, -1, -1):
            if find:
                  return
            result[depth] = i

            if depth == 0:
                  visited[i] = 1
                  findMax(depth + 1, result)
                  visited[i] = 0
            else:
                  if visited[i]:
                        continue
                  elif ineq[depth - 1] == "<" and result[depth - 1] > result[depth]:
                        break
                  elif ineq[depth - 1] == ">" and result[depth - 1] < result[depth]:
                        continue
                  else:
                        visited[i] = 1
                        findMax(depth + 1, result)
                        visited[i] = 0
def findMin(depth, result):
      global find
      if depth == k + 1:
            find = 1
            return
      for i in range(10):
            if find:
                  return
            result[depth] = i

            if depth == 0:
                  visited[i] = 1
                  findMin(depth + 1, result)
                  visited[i] = 0
            else:
                  if visited[i]:
                        continue
                  elif ineq[depth - 1] == "<" and result[depth - 1] > result[depth]:
                        break
                  elif ineq[depth - 1] == ">" and result[depth - 1] < result[depth]:
                        continue
                  else:
                        visited[i] = 1
                        findMin(depth + 1, result)
                        visited[i] = 0



k= int(input())
ineq = input().split()
result = [-1] * (k + 1)
visited = [0] * 10
find = 0
findMax(0, result)
print(''.join(str(a) for a in result))
find = 0
findMin(0, result)
print(''.join(str(a) for a in result))