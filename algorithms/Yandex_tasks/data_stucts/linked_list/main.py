from linked_list_YD import Node, LinkedList


if __name__ == '__main__':
    llist = LinkedList()
    # llist.add_first(Node(5))
    # llist.get_node(1)
    # llist.remove_node(1)
    # print(llist)
    with open('algorithms/Yandex_tasks/data_stucts/linked_list/in.txt', 'r') as f:
        info = f.read()
        for inf in info.split('\n')[1:]:
            if inf[0] == '1':
                llist.add_after(int(inf.split(' ')[1]),
                                Node(int(inf.split(' ')[2])))
            if inf[0] == '2':
                llist.get_node(int(inf.split(' ')[1]))
            if inf[0] == '3':
                llist.remove_node(int(inf.split(' ')[1]))
            print(llist)  
    # print(llist, llist.head, llist.tail)
    # llist.add_first(Node('aaa'))
    # print(llist, llist.head, llist.tail)
    # for node in llist:
    #     print(node)