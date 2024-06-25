class Node:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value

class BinaryTree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        new_node = Node(value)  
        if not self.root:
            self.root = new_node
            return    
        queue = [self.root]   
        while queue:
            node = queue.pop(0)  
            if not node.left:
                node.left = new_node
                return 
            if not node.right:
                node.right = new_node
                return
            if node.left:
                queue.append(node.left)  
            if node.right:
                queue.append(node.right)

    def inorder_traversal(self, node):
        result = []
        if node:
            result.extend(self.inorder_traversal(node.left))
            result.append(node.value)
            result.extend(self.inorder_traversal(node.right))
        return result

    def preorder_traversal(self, node):
        result = []
        if node:
            result.append(node.value)
            result.extend(self.preorder_traversal(node.left))
            result.extend(self.preorder_traversal(node.right))
        return result
    
    def postorder_traversal(self, node):
        result = []
        if node:
            result.extend(self.postorder_traversal(node.left))
            result.extend(self.postorder_traversal(node.right))
            result.append(node.value)
        return result
    
    def search_tree(self, node, value):
        if node == None:
            return False
        if node.value == value:
            return True 
        left_search = self.search_tree(node.left, value)
        if left_search:
            return True
        right_search = self.search_tree(node.right, value)
        if right_search:
            return True

def find_min(self, node):
    if node is None:
        return "tree empty"
    curr_min = node.value
    left_min = self.find_min(node.left)
    if left_min < curr_min:
        curr_min = left_min
    right_min = self.find_min(node.right)
    if right_min < curr_min:
        curr_min = right_min
    return curr_min

def find_max(self, node):
    if node is None:
        return "tree empty"
    curr_max = node.value
    left_max = self.find_max(node.left)
    if left_max > curr_max:
        curr_max = left_max
    right_max = self.find_max(node.right)
    if right_max > curr_max:
        curr_max = right_max
    return curr_max


tree = BinaryTree()
tree.insert(0)
tree.insert(1)
tree.insert(2)
tree.insert(3)
tree.insert(4)
tree.insert(5)
tree.insert(6)
tree.insert(7)

print(tree.search_tree(tree.root, 4))  # Output: True
print(tree.search_tree(tree.root, 6))  # Output: False

print(tree.inorder_traversal(tree.root))
print(tree.preorder_traversal(tree.root))
print(tree.postorder_traversal(tree.root))
