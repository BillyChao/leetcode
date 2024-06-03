# -*- coding:utf-8 -*-
# @FileName  :列表删除重复元素.py
# @Time      :2024/5/30 10:32 PM
# @Author    :mengchao01

def dedup(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


if __name__ == "__main__":
    items = [1, 4, 1, 3, 2, 1, 4, 3, 5]
    for i in dedup(items):
        print(i)
