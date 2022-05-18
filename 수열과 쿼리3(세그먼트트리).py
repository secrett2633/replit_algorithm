import sys
import math
from bisect import bisect_left
input = sys.stdin.readline

def init(node, start, end):
    if start == end :
        tree[node].append(A[start])
        return tree[node]
    else:
        temp = init(node*2, start, (start+end)//2) + init(node*2+1, (start+end)//2+1, end)
        for i in temp:
            tree[node].append(i)
        return tree[node]
def subSum(node, start, end, left, right, k):  
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return len(tree[node]) - bisect_left(tree[node], k + 1)
    return subSum(node*2, start, (start+end)//2, left, right, k) + subSum(node*2 + 1, (start+end)//2+1, end, left, right, k)
 

n = int(input())
A = list(map(int, input().split()))
tree = [[] for _ in range(2 ** math.ceil(math.log2(n) + 1))]

init(1, 0, n-1)
for i in tree:
  i.sort()
m = int(input())
last_ans = 0
for _ in range(m):
  a, b, c = map(int, input().rstrip().split())
  i = a ^ last_ans
  j = b ^ last_ans
  k = c ^ last_ans
  last_ans = subSum(1, 0, n - 1, i - 1, j - 1, k)
  print(last_ans)