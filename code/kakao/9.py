from collections import deque


def solution(board):
    size = len(board)
    answer = int(1e9)
    dp = [[int(1e9)] * size for _ in range(size)]
    # 북, 동, 남, 서
    distances = [(-1, 0, 0), (0, 1, 1), (1, 0, 2), (0, -1, 3)]
    q = deque()
    q.append([0, 0, 0, -1])  # x, y, cost, distance
    while q:
        x, y, cost, dist = q.popleft()
        if x == size - 1 and y == size - 1 and answer > cost:
            answer = cost
        for distance in distances:
            nx = x + distance[0]
            ny = y + distance[1]
            add = 1 if dist == distance[2] or dist == -1 else 6
            if not(0 <= nx < size and 0 <= ny < size) or board[nx][ny] == 1:
                continue
            if dp[nx][ny] < cost + add - 4:
                continue
            dp[nx][ny] = cost + add
            q.append([nx, ny, cost + add, distance[2]])

    return answer * 100
