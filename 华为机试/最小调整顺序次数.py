# https://fcqian.blog.csdn.net/article/details/128080305

num = int(input())
inputs = []
for i in range(num * 2):
    inputs.append(input())


def getResult(inputs: list):
    is_sorted = True
    size = 0
    tmp = []
    for input in inputs:
        if 'add' in input:
            if not tmp:
                tmp.append(input.split()[2])
            else:
                if 'head' in input:
                    is_sorted = False
                tmp.append(input.split()[2])
        else:
            if not is_sorted:
                size += 1
                is_sorted = True
            tmp.pop(0)
    return size


print(getResult(inputs=inputs))
