def solution(genres, plays):
    answer = []
    
    genre_dic = {}
    genre_dic_cnt = {}
    
    num = 0
    for genre, play in zip(genres,plays):
        if genre in genre_dic:
            genre_dic[genre].append((num, play))
            genre_dic_cnt[genre] += play
        else:
            genre_dic[genre] = [(num, play)]
            genre_dic_cnt[genre] = play
        num += 1
    # print(genre_dic)
    # {'classic': [(0, 500), (2, 150), (3, 800)], 'pop': [(1, 600), (4, 2500)]}
    
    for (k, v) in sorted(genre_dic_cnt.items(), key= lambda x : x[1], reverse=True):
    
        for (num, play) in sorted(genre_dic[k], key = lambda x : -x[1])[:2]:

            answer.append(num)
        
        
    return answer