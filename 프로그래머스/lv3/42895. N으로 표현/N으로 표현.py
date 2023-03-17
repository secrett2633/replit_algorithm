def solution(N, number):
    answer = 0
    res = [[0], [N]]
    if number == N: return 1
    if number == 0: return 2
    for i in range(2, 9):
        temp = set()
        if int(str(N) * i) != number: temp.add(int(str(N) * i))
        else: return i
        for cnt in range(1, i // 2 + 1):
            for j in res[cnt]:
                for k in res[i - cnt]:
                    if j + k != number: 
                        if j + k != 0: temp.add(j + k)
                    else: return i
                    if j - k != number: 
                        if j - k != 0: temp.add(j - k)
                    else: return i
                    if k - j != number: 
                        if k - j != 0: temp.add(k - j)
                    else: return i
                    if j * k != number: 
                        if j * k != 0: temp.add(j * k)
                    else: return i
                    if j // k != number: 
                        if j // k != 0: temp.add(j // k)
                    else: return i
                    if k // j != number: 
                        if k // j != 0: temp.add(k // j)
                    else: return i
        res.append(list(temp))
    return -1