# https://blog.csdn.net/qfc_128220/article/details/130633638

count = int(input())

coordinate_input = list(map(int, input().split()))
tree_num = int(input())


def getResult(coordinate):
    coordinate.sort()
    min_dis = 1
    max_dis = coordinate[-1]
    result = 1
    while min_dis <= max_dis:
        mid_dis = (min_dis + max_dis) >> 1
        if checkMid(mid_dis, coordinate):
            result = mid_dis
            min_dis = mid_dis + 1
        else:
            max_dis = mid_dis - 1
    return result


def checkMid(dis, coordinate):
    cur_pos = coordinate[0]
    tmp_count = 1
    for i in range(1, count):
        if coordinate[i] - cur_pos >= dis:
            tmp_count += 1
            cur_pos = coordinate[i]
    return tmp_count >= tree_num


print(getResult(coordinate_input))
