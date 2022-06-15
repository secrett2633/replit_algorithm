import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
def pre_order(x):
  print(x, end ="")
  if graph[x][0] != ".":
      pre_order(graph[x][0])
  if graph[x][1] != ".":
      pre_order(graph[x][1])

def in_order(x):    
  if graph[x][0] != ".":
      in_order(graph[x][0])
  print(x, end ="")
  if graph[x][1] != ".":
      in_order(graph[x][1])

def post_order(x):    
  if graph[x][0] != ".":
      post_order(graph[x][0])  
  if graph[x][1] != ".":
      post_order(graph[x][1])
  print(x, end ="")
    
n = int(input())
graph = dict()
for i in range(n):
  a, b, c = input().rstrip().split()
  graph[a] = [b, c]
  
pre_order("A")
print("")
in_order("A")
print("")
post_order("A")
print("")