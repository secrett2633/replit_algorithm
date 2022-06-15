import re
n=input()
if n.find('-') != -1:
    t=n.index('-')
    a=list(map(int,n[:t].split('+')))
    b=list(map(int,re.split('\+|\-',n[t:])[1:]))
else:
    a=list(map(int,n.split('+')))
    b=[0]
print(sum(a)-sum(b))