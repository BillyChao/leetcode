# 输入获取
n = int(input())
m = list(map(int, input().split()))
x = list(map(int, input().split()))


# 算法入口
def getResult(n, m, x):
    m.insert(0, 0)
    x.insert(0, 0)

    bag = 0
    for i in range(1, n + 1):
        bag += m[i] * x[i]

    dp = [False] * (bag + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(bag, m[i] - 1, -1):
            for k in range(1, x[i] + 1):
                if j >= m[i] * k:
                    if dp[j - m[i] * k]:
                        dp[j] = True

    return len(list(filter(lambda x: x, dp)))


# 算法调用
print(getResult(n, m, x))
