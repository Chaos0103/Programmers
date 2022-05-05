from itertools import permutations


def solution(user_id, banned_id):
    answer = []

    for users in list(permutations(user_id, len(banned_id))):
        check = True
        for i in range(len(banned_id)):
            if len(users[i]) != len(banned_id[i]):
                check = False
                break
            for j in range(len(users[i])):
                if users[i][j] == banned_id[i][j] or banned_id[i][j] == '*':
                    continue
                else:
                    check = False
                    break
        if check:
            users = list(users)
            users.sort()
            if users not in answer:
                answer.append(users)
    return len(answer)
