# https://blog.csdn.net/qfc_128220/article/details/129300607
import queue

num = int(input())
events = [input().split() for _ in range(num)]

import queue


class Custom():
    def __init__(self, number, pri):
        self.number = number
        self.pri = pri

    def __lt__(self, other):
        return self.pri < other.pri


def getResult(num, events):
    pri_q = queue.PriorityQueue()
    for event in events:
        if 'a' in event:
            pri_q.put(Custom(event[1], int(event[2])))
        elif 'p' in event:
            print(pri_q.get().number)


getResult(num, events)
