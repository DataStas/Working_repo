class Node(object):
    
    def __init__(self, val):
        self.val = val
        self.next = None


class MyLinkedList(Node):

    def __init__(self):
        self.tail = None
        self.head = None

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        for ind, node in enumerate(self):
            if ind == index:
                return node.val
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)
        node.next = self.head
        self.head = node

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        node = Node(val)

        if self.head is None:
            self.head = node
            return

        for current in self:
            pass
        current.next = node
        self.tail = node

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        node = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        if l

        prev_node = self.head
        for ind, current in enumerate(self):
            if ind == index:
                prev_node.next = node
                node.next = current
                return
            prev_node = current
        if ind+1 == index:
            self.addAtTail(val)
            return

    def __len__(self):
        size = 0
        for _ in self:
            size += 1
        return size

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index == 0:
            self.head = self.head.next
            return

        prev_node = self.head
        for ind, node in enumerate(self):
            if ind == index:
                prev_node.next = node.next
                return
            prev_node = node

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

if __name__ == "__main__":
    obj = MyLinkedList()
    obj.addAtHead(7)
    obj.addAtHead(2)
    obj.addAtHead(1)
    obj.addAtIndex(3, 0)
    print(obj)
    obj.deleteAtIndex(2)
    obj.addAtHead(6)
    obj.addAtTail(4)
    print(obj)
    print(obj.get(4))
    obj.addAtHead(4)
    obj.addAtIndex(5, 0)
    obj.addAtHead(6)
    print(obj)
    # obj.addAtHead(1)
    # obj.addAtTail(3)
    # obj.addAtIndex(1, 2)
    # print(obj)
    # print(obj.get(1))