def solution(s):
    answer = ''
    tmp = list(s.split())
    # print(tmp)
    # for word in tmp:
    #     if word == "":
    #         answer+= " "
    #     else:
    #         if word[0:1].isalpha():
    #             answer += word[0:1].upper() + word[1:].lower() + " "
    #             # print(answer)
    #         else:
    #             answer += word[0:1] + word[1:].lower() + " "    
    #         # answer += " "
    
    temp = s.split(' ')
    for i in temp:
        if i == '':
            answer += ' '
        else:
            answer += i[0].upper()+i[1:].lower() if len(i) > 1 else i.upper()
            answer += ' '
                    
    return answer[:-1]