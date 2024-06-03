# https://fcqian.blog.csdn.net/article/details/128061871?ydreferer=aHR0cHM6Ly9mY3FpYW4uYmxvZy5jc2RuLm5ldC9hcnRpY2xlL2RldGFpbHMvMTI3OTE0Mzgy
import functools

arr = input().split()


def getResult(arr: list):
    word_count = {}
    words = []
    for word in arr:
        word = ''.join(sorted(word))
        words.append(word)
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    words.sort(key=lambda x: (-word_count[x], len(x), x))
    return words


print(getResult(arr))
