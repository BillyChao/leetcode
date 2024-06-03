# https://fcqian.blog.csdn.net/article/details/128078962

arr = input().split()


def getResult(arr: list):
    arr.sort(key=lambda x: (len(x), x), reverse=True)
    for password in arr:
        exist = True
        for i in range(len(password) - 1, 1, -1):
            if password[0:i] not in arr:
                exist = False
                break
        if exist:
            return password


print(getResult(arr))
