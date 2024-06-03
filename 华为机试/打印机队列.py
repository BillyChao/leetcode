# https://fcqian.blog.csdn.net/article/details/128081817

event_cnt = int(input())

events = []
for _ in range(event_cnt):
    events.append(input())


def getResult(arr: list):
    index_dict = 1
    event_dict = {}
    for event in arr:
        if 'IN' in event:
            _, print_num, pri = event.split()
            if print_num not in event_dict:
                event_dict[print_num] = []
            event_dict[print_num].append((int(pri), index_dict))
            index_dict += 1
            event_dict[print_num].sort(key=lambda x: x[0], reverse=True)
        else:
            _, print_num = event.split()
            if event_dict[print_num]:
                print(event_dict[print_num].pop(0)[1])
            else:
                print('NULL')


getResult(events)
