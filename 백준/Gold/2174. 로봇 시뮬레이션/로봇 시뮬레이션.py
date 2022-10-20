import sys
input = sys.stdin.readline
d = {"N": (-1, 0), "W" : (0, -1), "E" : (0, 1), "S" : (1, 0)}
a, b = map(int, input().split())
graph = [[0] * a for _ in range(b)]
n, m = map(int, input().split())
robot = []
for i in range(n):
    r = list(input().rstrip().split())
    graph[b - int(r[1])][int(r[0]) - 1] = i + 1
    robot.append([b - int(r[1]), int(r[0]) - 1, r[2]])
flag = False
for _ in range(m):
    r = list(input().rstrip().split())
    if flag: continue
    i, cnt = int(r[0]) - 1, int(r[2])
    if r[1] == "L":
        for _ in range(cnt % 4):
            if robot[i][2] == "N": robot[i][2] = "W"
            elif robot[i][2] == "E": robot[i][2] = "N"
            elif robot[i][2] == "S": robot[i][2] = "E"
            else: robot[i][2] = "S"
    elif r[1] == "R":
        for _ in range(cnt % 4):
            if robot[i][2] == "N": robot[i][2] = "E"
            elif robot[i][2] == "E": robot[i][2] = "S"
            elif robot[i][2] == "S": robot[i][2] = "W"
            else: robot[i][2] = "N"
    else:
        for _ in range(cnt):
            graph[robot[i][0]][robot[i][1]] = 0
            robot[i][0], robot[i][1] = robot[i][0] + d[robot[i][2]][0], robot[i][1] + d[robot[i][2]][1]
            if 0 <= robot[i][0] < b and 0 <= robot[i][1] < a: 
                if graph[robot[i][0]][robot[i][1]]: print(f"Robot {i + 1} crashes into robot {graph[robot[i][0]][robot[i][1]]}"); flag = True; break 
            else: print(f"Robot {i + 1} crashes into the wall"); flag = True; break
            graph[robot[i][0]][robot[i][1]] = i + 1
if not flag: print("OK")