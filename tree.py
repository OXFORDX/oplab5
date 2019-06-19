from calc import polish
import operator


class Node:
    def __init__(self, left, root, right):
        self.root = root
        self.left = left
        self.right = right


class tree:
    def __init__(self):
        self.node_arr = []

    def add(self):
        x = polish('1 - (5 * 1 * 2 - 5 ^ 3) + 8')
        for i in x:
            print(i)
            if type(i[0]) is list and type(i[2]) is list:
                print(1)
                y, x = self.node_arr.pop(), self.node_arr.pop()
                self.node_arr.append(Node(y, i[1], x))
            elif type(i[0]) is list and type(i[2]) is int:
                print(2)
                x = self.node_arr.pop()
                self.node_arr.append(Node(x, i[1], i[2]))
            elif type(i[2]) is list and type(i[0]) is int:
                print(3)
                x = self.node_arr.pop()
                self.node_arr.append(Node(i[0], i[1], x))
            else:
                self.node_arr.append(Node(i[0], i[1], [2]))
        return self.node_arr[0]

    def postordereval(self, tree):
        print(tree.root)
        if type(tree.left) is not int:
            tree = tree.left
            print(tree)
            self.postordereval(tree)
        if type(tree.right) is not int:
            tree = tree.right
            print(tree)
            self.postordereval(tree)


tr = tree()
root = tr.add()
print(tr.postordereval(root))
