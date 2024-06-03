# https://fcqian.blog.csdn.net/article/details/128294577
import math

number = int(input())
code_arr = input().split()


def getResult(number, code_arr: list):
    codes = [(i, code_arr.count(i)) for i in set(code_arr)]
    codes.sort(key=lambda x: x[1], reverse=True)
    min_dis = len(code_arr)
    max_freq = codes[0][1]
    for i in codes:
        tmp = []
        if i[1] == max_freq:
            for j in range(number):
                if i[0] == code_arr[j]:
                    tmp.append(j)
            min_dis = min(min_dis, tmp[-1] - tmp[0] + 1)
    return min_dis


print(getResult(number, code_arr))
