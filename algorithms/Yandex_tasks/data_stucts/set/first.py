if __name__ == '__main__':
    # sset = set()
    # with open('Yandex_tasks/data_stucts/set/in.txt', 'r') as f:
    #     info = f.read()
    #     for inf in info.split('\n')[1:]:
    #         x = int(inf.split(' ')[1])
    #         if inf[0] == '1':
    #             sset = sset.union({x})
    #         if inf[0] == '2':
    #             if x in sset:
    #                 print(1)
    #             else:
    #                 print(0) 
    n = int(input())
    commands = []
    while n:
        commands.append(input())
        n -= 1
    sset = set()
    for inf in commands:
        x = int(inf.split(' ')[1])
        if inf[0] == '1':
            sset.add(x)
        if inf[0] == '2':
            if x in sset:
                print(1)
            else:
                print(0)