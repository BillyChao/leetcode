# -*- coding: utf-8 -*-

# 题目链接 https://fcqian.blog.csdn.net/article/details/128049270?ydreferer=aHR0cHM6Ly9mY3FpYW4uYmxvZy5jc2RuLm5ldC9hcnRpY2xlL2RldGFpbHMvMTI3OTE0Mzgy


head, n = input().split()

nodes = {}
for _ in range(int(n)):
    addr, val, next = input().split()
    nodes[addr] = [val, next]


def getResult(head, nodes):
    m = int(len(nodes) / 2)
    tmp = head
    for _ in range(m):
        tmp = nodes[tmp][1]
    return nodes[tmp][0]


if __name__ == '__main__':
    print(getResult(head, nodes))
