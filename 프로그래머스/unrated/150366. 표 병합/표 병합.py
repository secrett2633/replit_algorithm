def solution(commands):
    def change(target, value):
        for i in range(50):
            for j in range(50):
                if arr[i][j][0] == target[0]: 
                    arr[i][j] = value[::]
    answer = []
    arr = [[[0, ""] for _ in range(50)] for _ in range(50)]
    unique = 1
    for cmd in commands:
        command = cmd.split()
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c, v = int(command[1]) - 1, int(command[2]) - 1, command[3]
                if not arr[r][c][0]:
                    arr[r][c][1] = v
                else:
                    for i in range(50):
                        for j in range(50):
                            if arr[r][c][0] == arr[i][j][0]: arr[i][j][1] = v
            else:
                for i in range(50):
                    for j in range(50):
                        if arr[i][j][1] == command[1]: arr[i][j][1] = command[2][::]
        elif command[0] == "MERGE":
            r1, c1, r2, c2 = int(command[1]) - 1, int(command[2]) - 1, int(command[3]) - 1, int(command[4]) - 1
            if r1 == r2 and c1 == c2: continue #Merge해야 할 값이 같은경우 continue
            if arr[r1][c1][0] and arr[r2][c2][0]: #이미 둘 다 Merge가 되어있는 경우
                target, value = [arr[r2][c2][::], arr[r1][c1][::]] if arr[r1][c1][1] else [arr[r1][c1][::], arr[r2][c2][::]]
                change(target, value)
            elif arr[r1][c1][0]: #첫번째값이 Merge되어있는 경우                
                if arr[r1][c1][1]: arr[r2][c2] = arr[r1][c1][::]
                else:
                    arr[r2][c2][0] = arr[r1][c1][0]
                    target, value = arr[r1][c1][::], arr[r2][c2][::]
                    change(target, value)
            elif arr[r2][c2][0]: #두번째값이 Merge되어있는 경우                
                if arr[r1][c1][1]:
                    arr[r1][c1][0] = arr[r2][c2][0]
                    target, value = arr[r2][c2][::], arr[r1][c1][::]
                    change(target, value)
                else: arr[r1][c1] = arr[r2][c2][::]
            else: #Merge내역이 없는 경우
                arr[r1][c1][0] = unique; arr[r2][c2][0] = unique; unique += 1 
                if arr[r1][c1][1]: arr[r2][c2] = arr[r1][c1][::]
                else: arr[r1][c1] = arr[r2][c2][::]
        elif command[0] == "UNMERGE":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            tmp = arr[r][c][::]
            if tmp[0]:
                for i in range(50):
                    for j in range(50):
                        if arr[i][j][0] == tmp[0]: arr[i][j] = [0, ""]
                arr[r][c][1] = tmp[1][::]
            else: arr[r][c] = [0, tmp[1][::]]
        elif command[0] == "PRINT":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            answer.append(arr[r][c][1] if arr[r][c][1] else "EMPTY")
        # print(command)
        # for aaa in arr:
        #     print(*aaa)
        # print("===================")
    return answer