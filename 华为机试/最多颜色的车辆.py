# https://fcqian.blog.csdn.net/article/details/128063374
# 通过车辆的颜色信息
arr = input().split()
# 统计时间窗口
acc = input()


def getResult(arr, num):
    max_len = 1
    colors = {}
    for i in range(0, len(arr) - int(num) + 1):
        # 不需要每次都统计，滑动窗口，+1 -1
        for j in range(i, i + int(num)):
            if arr[j] not in colors:
                colors[arr[j]] = 0
            colors[arr[j]] += 1
        for v in colors.values():
            if max_len < v:
                max_len = v
        colors.clear()
    return max_len


def getResultNew(arr, num):
    colors = {}
    l, r = 0, int(num)
    for i in arr[l:r]:
        if i not in colors:
            colors[i] = 0
        colors[i] += 1
    max_len = max(colors.values())
    while r < len(arr):
        add = arr[r]
        remove = arr[l]
        l += 1
        r += 1
        if add not in colors:
            colors[add] = 0
        colors[add] += 1
        colors[remove] -= 1
        max_len = max(max_len, colors[add])
    return max_len


print(getResultNew(arr=arr, num=acc))
