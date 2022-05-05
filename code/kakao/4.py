def solution(stones, k):
    left, right = 1, 2 * (10**8)
    while left <= right:
        mid = (left + right) // 2
        count = 0
        for stone in stones:
            stone -= mid
            if stone <= 0:
                count += 1
            else:
                count = 0
            if count == k:
                break
        if count == k:
            right = mid - 1
        else:
            left = mid + 1

    return left
