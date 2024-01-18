# importing module 
from collections import deque


if __name__ == '__main__':
    llist = deque()
    with open('algorithms/Yandex_tasks/data_stucts/linked_list/in.txt', 'r') as f:
        info = f.read()
        for inf in info.split('\n')[1:]:
            if inf[0] == '1':
                x = int(inf.split(' ')[1])
                y = int(inf.split(' ')[2])
                if x == '0':
                    llist.appendleft(y)
                else:
                    llist.insert(x, y)
            if inf[0] == '2':
                print(llist)
                # llist[int(inf.split(' ')[1])]
            if inf[0] == '3':
                llist.pop(int(inf.split(' ')[1]))