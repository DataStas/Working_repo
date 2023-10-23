class TreeNode:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.key = key

#implementation of inorder traversal of a binary tree
def traverse_in_order(node: TreeNode):
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

def tree_height(node: TreeNode):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))


def tree_size(node: TreeNode):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


def is_bst(node: TreeNode):
    if node is None:
        return True, None, None

    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)

    is_bst_node = (is_bst_l and is_bst_r and
                   (max_l is None or node.key > max_l) and
                   (min_r is None or node.key < min_r))

    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key

if __name__ == "__main__":
    node0 = TreeNode(3)
    node1 = TreeNode(4)
    node2 = TreeNode(5)
    node0.left = node1
    node0.right = node2
