# https://fcqian.blog.csdn.net/article/details/129239766


word = input()


def getResult(word: str):
    alpha_dict = {}
    alpha_list = []
    for a in word:
        if a not in alpha_dict:
            alpha_dict[a] = 0
        alpha_dict[a] += 1

    for k, v in alpha_dict.items():
        alpha_list.append((k, v))
    alpha_list.sort(key=lambda x: x[0])
    single = ''
    result = []
    for i in alpha_list:
        if i[1] % 2 == 1 and single == '':
            single = i[0]
        result += [i[0]] * int(i[1] / 2)
    result = ''.join(result)
    result += single + result[::-1]
    return result


print(getResult(word))
