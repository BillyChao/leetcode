# -*- coding:utf-8 -*-
# @FileName  :超过50%的数字.py
# @Time      :2024/6/3 2:20 PM
# @Author    :mengchao01


def more_than_half(items):
    times = 0
    temp = None
    for item in items:
        if times == 0:
            temp = item
            times += 1
        else:
            if item == temp:
                times += 1
            else:
                times -= 1
    return temp


def list_depth(items):
    if isinstance(items, list):
        max_depth = 1
        for item in items:
            max_depth = max(1 + list_depth(item), max_depth)
        return max_depth
    else:
        return 0


if __name__ == "__main__":
    # print(more_than_half([1, 2, 3, 4, 5, 1, 1, 1, 1, 2]))
    print(list_depth([[1], 2, [[3]]]))
