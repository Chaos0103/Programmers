def solution(s):
    answer = []
    s = s[2:len(s) - 2]
    s = s.split('},{')
    for i in range(len(s)):
        s[i] = s[i].split(',')
    s.sort(key=lambda x: len(x))
    for part in s:
        for num in part:
            if int(num) not in answer:
                answer.append(int(num))
    return answer
    
