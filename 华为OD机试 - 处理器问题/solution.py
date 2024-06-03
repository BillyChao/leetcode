

# https://fcqian.blog.csdn.net/article/details/127914382
def getReuslt(arr, num):
    link1 = []
    link2 = []
    res = []
    for i in arr:
        if 0 <= i <= 3:
            link1.append(i)
        else:
            link2.append(i)
    len1 = len(link1)
    len2 = len(link2)
    if num == 1:
        if len1 == 1 or len2 == 1:
            if len1 == 1:
                res.append(link1)
            if len2 == 1:
                res.append(link2)
        elif len1 == 3 or len2 == 3:
            if len1 == 3:
                traverse(link1, 1, res)
            if len2 == 3:
                traverse(link2, 1, res)
        elif len1 == 2 or len2 == 2:
            if len1 == 2:
                traverse(link1, 1, res)
            if len2 == 2:
                traverse(link2, 1, res)
        elif len1 == 4 or len2 == 4:
            if len1 == 4:
                traverse(link1, 1, res)
            if len2 == 4:
                traverse(link2, 1, res)
    elif num == 2:
        if len1 == 2 or len2 == 2:
            if len1 == 2:
                traverse(link1, 2, res)
            if len2 == 2:
                traverse(link2, 2, res)
        elif len1 == 4 or len2 == 4:
            if len1 == 4:
                traverse(link1, 2, res)
            if len2 == 4:
                traverse(link2, 2, res)
        elif len1 == 3 or len2 == 3:
            if len1 == 3:
                traverse(link1, 2, res)
            if len2 == 3:
                traverse(link2, 2, res)
    elif num == 4:
        if len1 == 4 or len2 == 4:
            if len1 == 4:
                res.append(link1)
            if len2 == 4:
                res.append(link2)
    elif num == 8:
        if len1 == 4 and len2 == 4:
            res.append(link1 + link2)
    return res


def traverse(arr, count, res: list):
    if count == 1:
        for j in arr:
            res.append([j])
    elif count == 2:
        arr_len = len(arr)
        for i1 in range(0, arr_len):
            for i2 in range(i1 + 1, arr_len):
                res.append([arr[i1], arr[i2]])


if __name__ == '__main__':
    arr = [0, 1, 4, 5, 6, 7]
    num = 2
    result = getReuslt(arr=arr, num=num)
    print(result)
