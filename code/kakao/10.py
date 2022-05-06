def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for a, b in path:
        graph[a].append(b)
        graph[b].append(a)

    orders = [0] * n
    for a, b in order:
        orders[b] = a

    count = 0
    visited = [False] * n
    after = {}
    q = [0]
    while q:
        now = q.pop()
        if orders[now] and visited[orders[now]] == False:
            after[orders[now]] = now
            continue

        visited[now] = True
        count += 1

        for pos in graph[now]:
            if not visited[pos]:
                q.append(pos)

        if now in after:
            q.append(after[now])

    return n == count
