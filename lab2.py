class List_N1:
    def __init__(self):
        self.array = list()

    def get(self, idx):
        if len(self.array) == 0:
            return None
        return self.array[idx]

    def insert_value(self, value, idx):
        self.array.insert(idx, value)

    def remove(self, idx):
        self.array.pop(idx)

    def set(self, value, idx):
        self.array[idx] = value

    def print_list(self):
        print(self.array)


class List_N2:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def _check_len(self, idx):
        if self.len < idx or idx < 0:
            raise f"Index {idx} more than length list {self.len}"

    def get(self, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        return node.value

    def _push_to_end(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        node = self.root
        while node.next is not None:
            node = node.next
        new_node = self.Node(value)
        node.next = new_node

    def _push_to_begin(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        new_node = self.Node(value)
        new_node.next = self.root
        self.root = new_node

    def insert_value(self, value, idx):
        self._check_len(idx)
        if idx == 0:
            self._push_to_begin(value)
            return
        if idx == self.len:
            self._push_to_end(value)
            return
        self.len += 1
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next

        new_node = self.Node(value)
        new_node.next = node.next
        node.next = new_node
        return

    def _remove_to_begin(self):
        self.len -= 1
        if self.root.next is None:
            self.root = None
        else:
            self.root = self.root.next

    def _remove_to_end(self):
        idx = self.len
        self.len -= 1
        node = self.root
        while idx > 2:
            idx -= 1
            node = node.next
        node.next = None

    def remove(self, idx):
        self._check_len(idx)
        if idx == 0:
            self._remove_to_begin()
            return
        if idx == self.len:
            self._remove_to_end()
            return
        self.len -= 1
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next
        node.next = node.next.next

    def set(self, value, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        node.value = value

    def print_list(self):
        node = self.root
        res = f"["
        while node.next is not None:
            res += f"{node.value}, "
            node = node.next
        res += f"{node.value}]"
        print(res)


class List_N3:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None
            self.prev = None

    def __init__(self):
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def _check_len(self, idx):
        if self.len < idx or idx < 0:
            raise f"Index {idx} more than length list {self.len}"

    def get(self, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        return node.value

    def _push_to_end(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        node = self.root
        while node.next is not None:
            node = node.next
        new_node = self.Node(value)
        node.next = new_node
        new_node.prev = node

    def _push_to_begin(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        new_node = self.Node(value)
        self.root.prev = new_node
        new_node.next = self.root
        self.root = new_node

    def insert_value(self, value, idx):
        self._check_len(idx)
        if idx == 0:
            self._push_to_begin(value)
            return
        if idx == self.len:
            self._push_to_end(value)
            return
        self.len += 1
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next

        new_node = self.Node(value)

        new_node.prev = node
        node.next.prev = new_node
        new_node.next = node.next
        node.next = new_node

    def _remove_begin(self):
        self.len -= 1
        if self.root.next is not None:
            self.root.next.prev = None
        self.root = self.root.next
        return

    def _remove_end(self):
        self.len -= 1
        idx = self.len
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next
        node.next = None

    def set(self, value, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        node.value = value

    def remove(self, idx):
        self._check_len(idx)
        if idx == 0:
            self._remove_begin()
            return
        if idx == self.len - 1:
            self._remove_end()
            return
        self.len -= 1
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        node.next.prev = node.prev
        node.prev.next = node.next

    def print_list(self):
        node = self.root
        res = f"["
        while node.next is not None:
            res += f"{node.value}, "
            node = node.next
        res += f"{node.value}]"
        print(res)


class List_N4:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self):
        self.tail_link = None
        self.root = None
        self.len = 0

    def __len__(self):
        return self.len

    def _check_len(self, idx):
        if self.len < idx or idx < 0:
            raise f"Index {idx} more than length list {self.len}"

    def get(self, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        return node.value

    def _push_to_end(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        node = self.root
        while node.next is not None:
            node = node.next
        new_node = self.Node(value)
        node.next = new_node
        self.tail_link = new_node

    def _push_to_begin(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        new_node = self.Node(value)
        new_node.next = self.root
        self.root = new_node

    def insert_value(self, value, idx):
        self._check_len(idx)
        if idx == 0:
            self._push_to_begin(value)
            return
        if idx == self.len:
            self._push_to_end(value)
            return
        self.len += 1
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next

        new_node = self.Node(value)
        new_node.next = node.next
        node.next = new_node
        return

    def _remove_to_begin(self):
        self.len -= 1
        if self.root.next is None:
            self.root = None
        else:
            self.root = self.root.next

    def _remove_to_end(self):
        idx = self.len
        self.len -= 1
        node = self.root
        while idx > 2:
            idx -= 1
            node = node.next
        node.next = None
        self.tail_link = node

    def remove(self, idx):
        self._check_len(idx)
        if idx == 0:
            self._remove_to_begin()
            return
        if idx == self.len - 1:
            self._remove_to_end()
            return
        self.len -= 1
        node = self.root
        while idx > 1:
            idx -= 1
            node = node.next
        node.next = node.next.next

    def set(self, value, idx):
        self._check_len(idx)
        node = self.root
        while idx > 0:
            idx -= 1
            node = node.next
        node.value = value

    def print_list(self):
        node = self.root
        res = f"["
        while node.next is not None:
            res += f"{node.value}, "
            node = node.next
        res += f"{node.value}]"
        print(res)


class QueueN1:
    def __init__(self, limit):
        self.data = list()
        self.max_len = limit

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return "Limited queue"

    def put(self, value):
        if self.max_len <= len(self.data):
            self.data.pop(0)
        self.data.append(value)

    def get(self):
        return self.data.pop(0)

    @property
    def get_data(self):
        return self.data


class StackN1:
    def __init__(self, limit):
        self.data = list()
        self.max_len = limit

    def __str__(self):
        return "Limited stack"

    def __len__(self):
        return len(self.data)

    def put(self, value):
        if self.max_len <= len(self.data):
            self.data.pop()
        self.data.append(value)

    def get(self):
        return self.data.pop()

    @property
    def get_data(self):
        return self.data


class StackN2:
    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None

    def __init__(self, ):
        self.root = None
        self.len = 0

    def __str__(self):
        return "Stack on linked list"

    def __len__(self):
        return self.len

    def put(self, value):
        self.len += 1
        if self.root is None:
            self.root = self.Node(value)
            return
        new_node = self.Node(value)
        new_node.next = self.root
        self.root = new_node

    def get(self):
        value = self.root.value
        if self.root.next is not None:
            self.root = self.root.next
        else:
            self.root = None
        return value

    @property
    def get_data(self):
        node = self.root
        res = "[ "
        while node.next is not None:
            res += f"{node.value}, "
            node = node.next
        res += f"{node.value} ]"
        return res


def test_1():
    for idx, listik in enumerate([List_N1(), List_N2(), List_N3(), List_N4()]):
        print(f"Build list number {idx}")
        listik.insert_value(5, 0)
        listik.insert_value(4, 1)
        listik.insert_value(3, 2)
        listik.insert_value(2, 3)
        listik.print_list()
        print("Insert")
        listik.insert_value(10, 1)
        listik.insert_value(12, 0)
        listik.insert_value(12, 4)
        listik.print_list()
        print("Remove")
        listik.remove(6)
        listik.print_list()
        print("Get")
        print(listik.get(5))
        print("Insert")
        listik.insert_value(5, 0)
        listik.print_list()
        print("Set")
        listik.set(57, 0)
        listik.print_list()

        if idx == 3:
            print("Last element: ", listik.tail_link.value)
            print("Insert")
            listik.insert_value(5, 7)
            listik.print_list()
            print("Last element: ", listik.tail_link.value)


def test_2():
    for links in [QueueN1(3), StackN1(3), StackN2()]:
        print(f"DS {str(links)}")
        links.put(1)
        links.put(2)
        links.put(3)
        print("Queue: ", links.get_data)
        links.put(4)
        print("Queue: ", links.get_data)
        links.get()
        print("Queue: ", links.get_data)
        links.get()
        print("Queue: ", links.get_data)


if __name__ == "__main__":
    # test_1()
    test_2()
