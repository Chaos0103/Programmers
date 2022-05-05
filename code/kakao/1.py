def solution(board, moves):
    answer = 0
    deap = len(board)
    basket = []
    for move in moves:
        for i in range(deap):
            if board[i][move-1] != 0:
                basket.append(board[i][move-1])
                board[i][move-1] = 0
                break
        if len(basket) >= 2:
            if basket[len(basket) - 1] == basket[len(basket) - 2]:
                basket.pop()
                basket.pop()
                answer += 2
    return answer
