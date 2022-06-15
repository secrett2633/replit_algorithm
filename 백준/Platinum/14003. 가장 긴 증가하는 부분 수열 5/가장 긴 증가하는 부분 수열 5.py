import sys
from bisect import bisect_left

n=int(sys.stdin.readline())
a=list(map(int,sys.stdin.readline().split()))

q=[]
temp=[]
for x in a:
    if not q or x>q[-1]:
        q.append(x)
        temp.append((len(q)-1,x))
    else:
        idx = bisect_left(q,x)
        q[idx]=x
        temp.append((idx,x))

ans=[]
last_idx=len(q)-1
for i in range(len(temp)-1,-1,-1):
    if temp[i][0]==last_idx:
        ans.append(temp[i][1])
        last_idx-=1
print(len(ans))
print(*reversed(ans))