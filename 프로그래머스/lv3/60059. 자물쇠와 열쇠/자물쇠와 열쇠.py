def solution(key, lock):
    cnt = 0
    for i in range(len(lock)):
        for j in range(len(lock[0])):
            cnt += 1 - lock[i][j]
    if not cnt: return True
    for _ in range(4):
        for i in range(-len(key) + 1, len(key) + len(lock) + 1):
            for j in range(-len(key[0]) + 1, len(key[0]) + len(lock[0]) + 1):
                cnt1 = 0
                flag = False
                for x in range(len(key)):
                    for y in range(len(key[0])):
                        if 0 <= i + x < len(lock) and 0 <= j + y < len(lock[0]):
                            if not lock[i + x][j + y] and key[x][y]:
                                    cnt1 += 1
                            if lock[i + x][j + y] and key[x][y]:
                                flag = True                
                if cnt == cnt1 and not flag: return True
        key = [list(k[::-1]) for k in zip(*key)]    
    return False