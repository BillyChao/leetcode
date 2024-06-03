# https://fcqian.blog.csdn.net/article/details/128150865


max_weight, total = input().split()
arr = input().split()


def getResult(max_w, total, arr: list):
    arr.sort()
    max_w = int(max_w)
    arr = [int(num) for num in arr]
    l, r = 0, len(arr) - 1
    need = 0
    while l <= r:
        if arr[r] + arr[l] > max_w:
            r -= 1
        else:
            r -= 1
            l += 1
        need += 1
    return need


print(getResult(max_weight, total, arr))
