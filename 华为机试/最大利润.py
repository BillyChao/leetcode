# https://fcqian.blog.csdn.net/article/details/128249510


goods_num = int(input())
sale_days = int(input())
goods_store = list(map(int, input().split()))
goods_price = []
for _ in range(goods_num):
    goods_price.append(list(map(int, input().split())))


def getResult(goods_num, sale_days, goods_store, goods_price):
    max_profit = 0
    for i in range(goods_num):
        price = goods_price[i]
        for j in range(sale_days - 1):
            if price[j] < price[j + 1]:
                max_profit += (price[j + 1] - price[j]) * goods_store[i]
    return max_profit


print(getResult(goods_num, sale_days, goods_store, goods_price))
