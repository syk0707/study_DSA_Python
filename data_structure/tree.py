import random
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __init__(self, value, left, right):
        self.parent = -1
        self.data = value
        self.left_node = left
        self.right_node = right


class NodeMgmt:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left is not None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right is not None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if not searched:
            return False

        if self.current_node.left is None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node
        elif self.current_node.left is not None and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left
        elif self.current_node.left is None and self.current_node.right is not None:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right
        elif self.current_node.left is not None and self.current_node.right is not None:
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.change_node.left
            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left is not None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right is not None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left
        return True


tree = {}
level_min = []
level_max = [0]
x = 1
level_depth = 1


def pre_order(node):
    sys.stdout.write(f"{node.data}")
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])


def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    sys.stdout.write(f"{node.data}")
    if node.right_node != '.':
        in_order(tree[node.right_node])


def in_order(node, level):
    global level_depth, x
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
    level_min[level] = min(level_min[level], x)
    level_max[level] = max(level_max[level], x)
    x += 1
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)


def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    sys.stdout.write(f"{node.data}")


def tree_1991():
    n = int(sys.stdin.readline())
    for i in range(n):
        data, left_node, right_node = sys.stdin.readline().split()
        tree[data] = Node(data, left_node, right_node)
    pre_order(tree['A'])
    sys.stdout.write(f"\n")
    in_order(tree['A'])
    sys.stdout.write(f"\n")
    post_order(tree['A'])


def tree_2250():
    n = int(sys.stdin.readline())
    root = -1
    level_min.append(n)

    for i in range(1, n + 1):
        tree[i] = Node(i, -1, -1)
        level_min.append(n)
        level_max.append(0)

    for _ in range(n):
        number, left_node, right_node = map(int, sys.stdin.readline().split())
        tree[number].left_node = left_node
        tree[number].right_node = right_node
        if left_node != -1:
            tree[left_node].parent = number
        if right_node != -1:
            tree[right_node].parent = number

    for i in range(1, n + 1):
        if tree[i].parent == -1:
            root = i

    in_order(tree[root], 1)

    result_level = 1
    result_width = level_max[1] - level_min[1] + 1
    for i in range(2, level_depth + 1):
        width = level_max[i] - level_min[i] + 1
        if result_width < width:
            result_level = i
            result_width = width

    sys.stdout.write(f"{result_level} {result_width}")


if __name__ == "__main__":
    # bst_nums = set()
    # for num in range(100):
    #     bst_nums.add(num)
    # head = Node(50)
    # binary_tree = NodeMgmt(head)
    # for num in bst_nums:
    #     binary_tree.insert(num)
    # for num in bst_nums:
    #     if not binary_tree.search(num):
    #         print('search failed', num)
    # delete_nums = set()
    # bst_nums = list(bst_nums)
    # while len(delete_nums) != 10:
    #     delete_nums.add(bst_nums[random.randint(0, 99)])
    # for before_delete_num in delete_nums:
    #     print(f"{before_delete_num} in tree : {binary_tree.search(before_delete_num)}")
    # for del_num in delete_nums:
    #     if not binary_tree.delete(del_num):
    #         print('delete failed', del_num)
    #     print(f"{del_num} in tree : {binary_tree.search(del_num)}")
    # tree_1991()
    tree_2250()

