def solution(s):
    answer = ''
    number = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7",
              "eight": "8", "nine": "9"}
    for i in range(len(s)):
        if s[i].isdigit():
            answer += s[i]
        else:
            for step in range(3, 6):
                if s[i:i+step] in number.keys():
                    answer += number[s[i:i+step]]
                    break
    return int(answer)
