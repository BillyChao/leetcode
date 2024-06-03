# https://fcqian.blog.csdn.net/article/details/128075040

number = input()
black_str = input()

mapping = ["abc", "def", "ghi", "jkl", "mno", "pqr", "st", "uv", "wx", "yz"]

result = []


def getResult(num, black):
    #
    index = 0
    str_len = len(num)
    getAllCollection(num, index, '', black)


def getAllCollection(num, index, tmp_str, filter_str):
    if index == len(num):
        if tmp_str.find(filter_str) == -1:
            result.append(tmp_str)
        return
    for a in mapping[int(num[index])]:
        tmp_str += a
        getAllCollection(num, index + 1, tmp_str, filter_str)
        # 回退到上一层
        tmp_str = tmp_str[:-1]


getResult(number, black_str)
print(result)
