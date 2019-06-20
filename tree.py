from calc import polish
import operator


class Node:
    def __init__(self, left, root, right):
        self.root = root
        self.left = left
        self.right = right


class tree:
    def __init__(self, calc):
        self.node_arr = []
        self.calc = calc

    def add(self):
        x = polish(self.calc)
        for i in x:
            if type(i[0]) is list and type(i[2]) is list:
                y, x = self.node_arr.pop(), self.node_arr.pop()
                self.node_arr.append(Node(y, i[1], x))
            elif type(i[0]) is list and type(i[2]) is int:
                x = self.node_arr.pop()
                self.node_arr.append(Node(x, i[1], i[2]))
            elif type(i[2]) is list and type(i[0]) is int:
                x = self.node_arr.pop()
                self.node_arr.append(Node(i[0], i[1], x))
            else:
                self.node_arr.append(Node(i[0], i[1], i[2]))
        return self.node_arr[0]

    def preorder(self, tree):
        if type(tree) is not int:
            print('---node---')
            print('root: ', tree.root)
            print('left: ', tree.left)
            print('right: ', tree.right)
            print('---endnode---')
            print('-->left')
            self.preorder(tree.left)
            print('-->right')
            self.preorder(tree.right)

    def answer(self):
        return polish(self.calc).calc()


tr = tree('2 - 3 / (4 * 5 - 1) ^ (4 - 1)')
root = tr.add()
tr.preorder(root)
print(tr.answer())
