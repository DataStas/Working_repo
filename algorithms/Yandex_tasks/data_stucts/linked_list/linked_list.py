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
            nodes.append(node.val)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('Linked list is empty')
        else:
            for node in self:
                if node.val == target_node_data:
                    new_node.next = node.next
                    node.next = new_node
                    return
        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception('Linked list is empty')

        if self.head.val == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head
        for node in self:
            if node.val == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception('Linked list is empty')

        if self.head.val == target_node_data:
            self.head = self.head.next
            return

        prev_node = self.head
        for node in self:
            if node.data == target_node_data:
                prev_node.next = node.next
                return
            prev_node = node
        
        raise Exception("Node with data '%s' not found" % target_node_data)