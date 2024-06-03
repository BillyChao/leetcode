# https://fcqian.blog.csdn.net/article/details/128156698
import math

coupon = list(map(int, input().split()))
total_num = int(input())
total_price = [int(input()) for _ in range(total_num)]


def getResult(coupon: list, total_num, total_price):
    no_rule = coupon[2] * 5
    for i in range(total_num):
        coupon_num = 0
        price = total_price[i]
        if price >= 100:
            # >100 先使用满减券
            for _ in range(coupon[0]):
                price -= math.floor(price / 100) * 10
                coupon_num += 1
                if price < 100:
                    break
            # 是否用打折
            if coupon[1] > 0 and math.ceil(price * 0.08) >= no_rule:
                price = math.floor(price * 0.92)
                coupon_num += 1
            else:
                price -= no_rule
                coupon_num += coupon[2]
        else:
            if coupon[1] > 0 and math.ceil(price * 0.08) > 5:
                coupon_num += 1
                price = math.floor(price * 0.92)
            rule_cnt = min(math.ceil(price / 5), coupon[2])
            coupon_num += rule_cnt
            price = max(0, price - rule_cnt * 5)
        print(price, coupon_num)


getResult(coupon, total_num, total_price)
