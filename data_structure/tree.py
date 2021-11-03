import random
import sys


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __init__(self, value, left, right):
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
    tree_1991()

