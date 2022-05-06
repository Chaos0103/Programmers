from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def solution(places):
    answer = [1] * 5

    for k in range(5):
        for i in range(5):
            for j in range(5):
                if places[k][i][j] == 'P':
                    if not bfs(i, j, places[k]):
                        answer[k] = 0
    return answer


def bfs(x, y, graph):
    visited = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((x, y, 0))
    visited[x][y] = 1
    while q:
        x, y, time = q.popleft()
        if graph[x][y] == 'P' and time != 0:
            return False
        if time == 2:
            continue
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 5 or ny >= 5:
                continue
            if visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                visited[nx][ny] = 1
                q.append((nx, ny, time + 1))
    return True
