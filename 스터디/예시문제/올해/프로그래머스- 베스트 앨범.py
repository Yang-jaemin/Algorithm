def solution(genres, plays):
    hass = {}
    tmp = []
    answer = []
    setting_genres = []
    # 장르별로 해쉬 생성
    for i in range(len(genres)):
        if genres[i] not in hass:      
            hass[genres[i]] = plays[i]
        else:
            hass[genres[i]] += plays[i]
    # 해쉬의 정보를 튜플로 묶어서 정렬 -> 재생수 많은 장르순으로 정렬해야해서        
    for j,l in hass.items():
        setting_genres.append((j,l))
    setting_genres.sort(key = lambda x : (x[1],x[0]),reverse = True) # 재생수를 key로 정렬하는데 reverse 걸어서 큰것부터(내림차순)
 
    # 이제 재생수 많은 장르부터 2곡씩 뺀다
    for q,w in setting_genres:
        for k in range(len(genres)):
            if genres[k] == q: 
                tmp.append((plays[k],k))
        tmp.sort(reverse = True) # 내림차순으로 해야 재생수 많은게 앞으로 온다
        
        if len(tmp) == 1:           # 곡이 1개만 있을 수도 있고
            answer.append(tmp[0][1])
        elif tmp[0][0] == tmp[1][0]:# 두곡이 재생수가 같으면
            answer.append(tmp[1][1])# 작은 곡부터
            answer.append(tmp[0][1])
        else:
            answer.append(tmp[0][1])# 이미 크기에따라서 정렬했으니까 그냥 앞부터
            answer.append(tmp[1][1])
        tmp.clear()
        
    return answer   






def solution(genres, plays):
    play_count = {} # str(genre) to int
    song_lists = {} # str(genre) to list of (int(songID), int)
    
    for i in range(len(genres)):
        genre = genres[i]
        if genre not in play_count:
            play_count[genre] = 0
            song_lists[genre] = []
        # 장르별로 곡 목록을 유지하는데 (-(재생 횟수) 높은거가 우선, 고유 번호 낮은게 우선)
        play_count[genre] += plays[i]
        song_lists[genre].append((-plays[i], i))

    play_count_sorted = []
    for genre, count in play_count.items():
        play_count_sorted.append((count, genre))
    play_count_sorted.sort(reverse=True)
    
    answer = []
    for _, genre in play_count_sorted:
        song_list = song_lists[genre]
        song_list.sort()
        if len(song_list) > 2:
            song_list = song_list[:2]
        for _, id in song_list:
           answer.append(id)
    return answer

# [(-500, 2), (-500, 1), (-300, 0)]
# [(-500, 1), (-500, 2), (-300, 0)]