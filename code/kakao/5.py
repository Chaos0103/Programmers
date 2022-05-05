import sys
sys.setrecursionlimit(10000)


def solution(k, room_number):
    answer = []
    rooms = dict()
    for num in room_number:
        room = findRoom(rooms, num)
        answer.append(room)
    return answer


def findRoom(rooms, num):
    if num not in rooms:
        rooms[num] = num + 1
        return num
    empty = findRoom(rooms, rooms[num])
    rooms[num] = empty + 1
    return empty
