# -*- coding:utf-8 -*-
# @FileName  :重试装饰器.py
# @Time      :2024/6/3 3:43 PM
# @Author    :mengchao01
import time
from functools import wraps
import random


class CustomError(Exception):
    """自定义异常类"""
    pass


def retry(times=3, max_delay=10, errors=(CustomError,)):
    """
    可以给retru 传入自定义参数
    :param times:
    :param max_delay:
    :param errors:
    :return:
    """

    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                try:
                    return f(*args, **kwargs)
                except errors as e:
                    # 重试三次 每次sleep 随机时间
                    rand_delay = random.randint(1, max_delay)
                    time.sleep(rand_delay)
                    print(f'sleep {rand_delay}s...')

        return wrapper

    return decorator


@retry()
def load_data():
    raise CustomError('custom error')


if __name__ == '__main__':
    print(load_data())
