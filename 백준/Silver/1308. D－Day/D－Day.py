import sys
from datetime import datetime
input = sys.stdin.readline
def cal(now):
    d = 0    
    for i in range(now, now + 1000):
        if i % 400 == 0:
            d += 366
        elif i % 100 == 0:
            d += 365
        elif i % 4 == 0:
            d += 366
        else:
            d += 365            
    return d

def solve(today, dday):
    a = datetime(year=today[0], month=today[1], day=today[2])
    b = datetime(year=dday[0], month=dday[1], day=dday[2])    
    c = (b - a).days    
    d = cal(now=today[0])    
    if c >= d:
        c = "gg"
    else:
        c = f"D-{c}"    
    return c
  
today = list(map(int, input().split()))
dday = list(map(int, input().split()))
print(solve(today, dday))