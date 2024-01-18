class Node():
    def __init__(self, val, next=None) -> None:
        self.next = next
        self.val = val

    def __repr__(self):
        return self.val


class LinkedList(Node):
    def __init__(self, nodes=None) -> None:
        self.head = None
        self.tail = None
        if nodes:
            node = Node(val=nodes.pop())
            self.tail = node
            node = Node(val=nodes.pop(0))
            self.head = node
            for el in nodes:
                node.next = Node(val=el)
                node = node.next
            node.next = self.tail

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.val))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node: Node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, index, new_node: Node):
        if index == 0:
            self.add_first(new_node)
            return

        for ind, node in enumerate(self):
            if ind == index-1:
                new_node.next = node.next
                node.next = new_node
                return
        raise Exception("Node with index '%s' not found" % index)

    def remove_node(self, index: int):
        if self.head is None:
            raise Exception('Linked list is empty')

        if self.head.next is None:
            self.head = None
            return
        
        prev_node = self.head
        for ind, node in enumerate(self):
            if ind == index-1:
                prev_node.next = node.next
                return
            prev_node = node

        raise Exception("Node with index '%s' not found" % index)

    def get_node(self, index: int) -> Node:
        for ind, node in enumerate(self):
            if index-1 == ind:
                print(node.val)
                return

if __name__ == '__main__':
    llist = LinkedList()
    n = int(input())
    commands = []
    while n:
        commands.append(input())
        n -= 1
    for inf in commands:
        if inf[0] == '1':
            llist.add_after(int(inf.split(' ')[1]),
                            Node(int(inf.split(' ')[2])))
        if inf[0] == '2':
            llist.get_node(int(inf.split(' ')[1]))
        if inf[0] == '3':
            llist.remove_node(int(inf.split(' ')[1])) 