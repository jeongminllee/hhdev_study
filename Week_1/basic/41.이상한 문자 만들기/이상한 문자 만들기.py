def solution(s):
    answer = ''
    index = 0
    for i in range(len(s)) :
        if s[i] == ' ' :
            answer += s[i]
            index = 0
        else :
            if index % 2 == 0 :
                answer += s[i].upper()
                index += 1
            else :
                answer += s[i].lower()
                index += 1
    return answer