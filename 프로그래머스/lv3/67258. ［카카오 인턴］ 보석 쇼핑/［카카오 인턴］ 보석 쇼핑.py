def solution(gems):
    key = list(set(gems))
    lenkey = len(key)
    lengems = len(gems)
    cache = {key[i]:i for i in range(lenkey)}
    now = [0] * lenkey
    answer = [[lengems - 1, 1, lengems]]
    i, j = 0, 0
    while j < lengems and i < lengems:        
        if all(now): 
            answer.append([j - i - 1, i + 1, j])
            now[cache[gems[i]]] -= 1
            i += 1
        else:
            now[cache[gems[j]]] += 1
            j += 1
    while all(now): 
        answer.append([j - i - 1, i + 1, j])
        now[cache[gems[i]]] -= 1
        i += 1
    answer.sort(key = lambda x:(x[0], x[1], x[2]))
    return answer[0][1:]