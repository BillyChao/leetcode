# -*- coding: utf-8 -*-

"""
@Time    : 2021/3/2 4:39 下午
@Author  : mc
@File    : solution.py
@Software: PyCharm
"""


class CQueue:

    def __init__(self):
        self.in_heap = []
        self.out_headp = []

    def appendTail(self, value: int) -> None:
        while self.out_headp:
            self.in_heap.append(self.out_headp.pop())
        self.in_heap.append(value)

    def deleteHead(self) -> int:
        while self.in_heap:
            self.out_headp.append(self.in_heap.pop())
        if not self.out_headp:
            return -1
        return self.out_headp.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()
c_queue = CQueue()
c_queue.appendTail(1)
c_queue.appendTail(2)
c_queue.appendTail(3)
print(c_queue.deleteHead())
print(c_queue.deleteHead())
print(c_queue.deleteHead())
