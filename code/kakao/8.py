def solution(n, k, cmd):
    answer = ['O'] * n
    # data = elem: (prev, next)
    data = {i: [i - 1, i + 1] for i in range(n)}
    delete = []
    for cm in cmd:
        cm = cm.split()
        if cm[0] == 'U':
            for _ in range(int(cm[1])):
                k = data[k][0]
        elif cm[0] == 'D':
            for _ in range(int(cm[1])):
                k = data[k][1]
        elif cm[0] == 'C':
            prev, next = data[k]
            delete.append((prev, next, k))
            answer[k] = 'X'
            if next == n:
                data[prev][1] = next
                k = prev
            elif prev == -1:
                data[next][0] = prev
                k = next
            else:
                data[prev][1] = next
                data[next][0] = prev
                k = next
        elif cm[0] == 'Z':
            prev, next, elem = delete.pop()
            answer[elem] = 'O'
            if next == n:
                data[prev][1] = elem
            elif prev == -1:
                data[next][0] = elem
            else:
                data[prev][1] = elem
                data[next][0] = elem

    return ''.join(answer)
