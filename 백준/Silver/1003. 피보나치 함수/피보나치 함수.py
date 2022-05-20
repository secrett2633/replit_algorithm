import sys
input = sys.stdin.readline

def fibonacci(n):
    if n == 0:
        list1[0] += 1
        return 0
    elif n == 1:
        list1[1] += 1
        return 1
    else:
        if visited[n - 1] == []:
          temp = list1[0]
          temp1 = list1[1]
          visited[n - 1] = fibonacci(n - 1)
          arr[n - 1] = [list1[0] - temp, list1[1] - temp1]
        else:
          list1[0] += arr[n - 1][0]
          list1[1] += arr[n - 1][1]
          
        if visited[n - 2] == []:
          temp = list1[0]
          temp1 = list1[1]
          visited[n - 2] = fibonacci(n - 2)
          arr[n - 2] = [list1[0] - temp, list1[1] - temp1]
          
        else:
          list1[0] += arr[n - 2][0]
          list1[1] += arr[n - 2][1]
          
        return visited[n - 1] + visited[n - 2]
      
t = int(input())
for i in range(t):
  n = int(input())
  list1 = [0, 0]
  visited = [[] for i in range(n + 1)]
  arr = [[] for i in range(n + 1)]
  fibonacci(n)  
  print(str(list1[0]) + " " + str(list1[1]))