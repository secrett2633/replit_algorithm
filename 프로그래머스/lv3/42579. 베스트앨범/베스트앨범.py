def solution(genres, plays):
    answer = []
    cache = list(set(genres))    
    cache = {cache[i]:i for i in range(len(cache))}
    visited = [[0] for _ in range(len(cache))]
    for i in range(len(plays)):
        visited[cache[genres[i]]][0] += plays[i]
        visited[cache[genres[i]]].append([plays[i], i])
    visited.sort(key = lambda x:x[0], reverse = True)
    for arr in visited:
        new_arr = arr[1:]
        new_arr.sort(key = lambda x:x[0], reverse = True)
        for i in range(2):
            try: answer.append(new_arr[i][1])
            except: continue         
    return answer