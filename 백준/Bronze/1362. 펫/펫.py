import sys
input = sys.stdin.readline
for i in range(1, 100000):
    o, w = map(int, input().split())
    if o == 0 and w == 0: break
    flag = False
    while True:
        a, b = input().split()
        if a == "#" and b == "0": break
        if a == "F": w += int(b)
        else: w -= int(b)
        if w <= 0: flag = True
    if flag: print(f"{i} RIP")
    elif o / 2 < w < 2 * o: print(f"{i} :-)")
    else: print(f"{i} :-(")
    