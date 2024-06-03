# https://fcqian.blog.csdn.net/article/details/128151648
# https://leetcode.cn/problems/partition-to-k-equal-sum-subsets/solutions/1441006/by-lfool-d9o7/

# 输入获取
m = int(input())
link = list(map(int, input().split()))


# 算法入口
def getResult(link, m):
    link.sort(reverse=True)

    sumV = 0
    for ele in link:
        sumV += ele

    while m > 0:
        if canPartitionMSubsets(link[:], sumV, m):
            return int(sumV / m)
        m -= 1

    return sumV


def canPartitionMSubsets(link, sumV, m):
    if sumV % m != 0:
        return False

    subSum = sumV / m

    if subSum < link[0]:
        return False

    while len(link) > 0 and link[0] == subSum:
        link.pop(0)
        m -= 1

    buckets = [0] * m

    return partition(link, 0, buckets, subSum)


def partition(link, index, buckets, subSum):
    if index == len(link):
        return True

    select = link[index]

    for i in range(len(buckets)):
        if i > 0 and buckets[i] == buckets[i - 1]:
            continue

        if select + buckets[i] <= subSum:
            buckets[i] += select
            if partition(link, index + 1, buckets, subSum):
                return True
            buckets[i] -= select

    return False


# 算法调用
print(getResult(link, m))
