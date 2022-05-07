def solution(gems):
    answer = [1, len(gems)]
    cnt = len(list(set(gems)))
    left, right = 0, 0
    data = dict()
    data[gems[0]] = 1
    while True:
        if len(data) == cnt:
            if abs(answer[1] - answer[0]) > abs(right - left):
                print(right, left)
                answer[0], answer[1] = left + 1, right + 1
            if data[gems[left]] == 1:
                del data[gems[left]]
            else:
                data[gems[left]] -= 1
            left += 1
        else:
            right += 1
            if left >= len(gems) or right >= len(gems):
                break
            if gems[right] in data:
                data[gems[right]] += 1
            else:
                data[gems[right]] = 1
    return answer
