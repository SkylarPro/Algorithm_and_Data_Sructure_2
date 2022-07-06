import operator
class Tree:
    class Node:
        def __init__(self, value, operation=None):
            self.value = value
            self.operation = operation
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None
        self.len = 0

    def _insert(self, root, value, operation=None):
        if value < root.value:
            if not root.left is None:
                return self._insert(root.left, value,operation)
            else:
                root.left = self.Node(value, operation)
        elif value > root.value:
            if not root.right is None:
                return self._insert(root.right, value,operation)
            else:
                root.right = self.Node(value, operation)
        return root

    def insert(self, value, operation=None):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value, operation)
            return
        self._insert(self.root, value, operation)
        return True

    def _find(self, root, value):
        if root.value == value:
            self.find_flag = 1
        if root.value > value:
            if not root.left is None:
                self._find(root.left, value)
        else:
            if not root.right is None:
                self._find(root.right, value)
        return False

    def find(self, value):
        self.find_flag = 0
        self._find(self.root, value)
        if self.find_flag == 1:
            return True

    def right_left_node(self, root, depth):
        if depth == 0:
            self.right_left_node(root.right, 1)
        else:
            if not root.left is None:
                self.right_left_node(root.left, 1)
                if self.flag == 1:
                    root.left = root.left.right
                    self.flag = 0
                if self.flag == 2:
                    root.left = None
            else:
                self.node_info = root.value
                self.flag = 2
                if not root.right is None:
                    self.flag = 1

    def _remove(self, root, value):
        if root.value == value:
            if root.left is None and root.right is None:
                self.mode = "zero"
            if root.left is None and not root.right is None:
                self.mode = "ones_right"
            if not root.left is None and root.right is None:
                self.mode = "ones_left"
            if not root.left is None and not root.right is None:
                self.mode = "double"
        elif root.value > value:
            self._remove(root.left, value)
            if self.mode == "zero":
                root.left = None
                self.mode = None
            if self.mode == "ones_right":
                root.left = root.left.right
                self.mode = None
            if self.mode == "ones_left":
                root.left = root.left.left
                self.mode = None
            if self.mode == "double":
                self.mode = None
                if root.left.right.left is None:
                    node = root.left.left
                    root.left = root.left.right
                    root.left.left = node
                else:
                    self.right_left_node(root.left, 0)
                    root.left.value = self.node_info

        else:
            self._remove(root.right, value)
            if self.mode == "zero":
                root.right = None
                self.mode = None
            if self.mode == "ones_right":
                root.right = root.right.right
                self.mode = None
            if self.mode == "ones_left":
                root.right = root.right.left
                self.mode = None
            if self.mode == "double":
                self.mode = None
                if root.right.right.left is None:
                    node = root.right.left
                    root.right = root.right.right
                    root.right.left = node
                else:
                    self.right_left_node(root.right, 0)
                    root.right.value = self.node_info

    def remove(self, value):
        if self.find(value):
            self.mode = None
            self.node_info = None
            self.flag = False
            self._remove(self.root, value)
        return False

    def _dfs(self, root):
        print(root.value)
        if not root.left is None:
            self._dfs(root.left)
        if not root.right is None:
            self._dfs(root.right)
        return

    def _symmetric(self, root):
        if root is None:
            return
        self._symmetric(root.left)
        print(root.value)
        self._symmetric(root.right)


    def _terminal(self, root,):
        if root is None:
            return
        self._terminal(root.left)
        self._terminal(root.right)
        print(root.value)


    def symmetric(self):
        "обратный"
        self._symmetric(self.root)

    def terminal(self,):
        "концевой"
        self._terminal(self.root)

    def direct_line(self):
        "прямой"
        self._dfs(self.root)

    def _get_operation(self, root,):
        if root is None:
            return
        self._get_operation(root.left)
        self._get_operation(root.right)
        self.expression.append((root.value, root.operation))

    def compute_tree(self):
        self.expression = []
        res = 0
        self._get_operation(self.root)
        hashh = []
        for i in range(len(self.expression)):
            curr, op = self.expression[i]
            if op is None:
                hashh.append(curr)
            if not op is None:
                res = op(hashh[0], hashh[1])
                print(f"Step {i} res:{res}")
                hashh.clear()
                hashh.append(res)
        return hashh[0]





if __name__=="__main__":
    tree = Tree()
    tree.insert(8)
    tree.insert(3)
    tree.insert(10)
    tree.insert(1)
    tree.insert(6)
    tree.insert(4)
    tree.insert(7)
    tree.insert(14)
    tree.insert(13)

    print(f"Find 13 {tree.find(13)}")
    # print("Прямой обход")
    # tree.direct_line()
    # tree.insert(20, operator.add)
    # tree.insert(15, operator.mul)
    # tree.insert(10, operator.sub)
    # tree.insert(7)
    # tree.insert(14)
    # tree.insert(16)
    # tree.insert(40)
    # print("Remove")
    # tree.remove(6)
    # tree.terminal()
    # print("Remove")
    # print(tree.compute_tree())