# Alpha version of parsing
from tree import tree


class file_parse:
    def __init__(self, file):
        self.file = file
        self.container = []
        self.values = {}
        self.task = {}
        self.filling()

    def parse_str(self):
        with open(self.file, 'r') as file:
            for i in file:
                if '\n' in i:
                    self.container.append(i[:-1].replace(' ', ''))
                else:
                    self.container.append(i.replace(' ', ''))
        return self.container

    def filling(self):
        container = self.parse_str()
        for i, j in enumerate(container):
            s = ''
            if '[' not in j or ']' not in j:
                for x, y in enumerate(j):
                    if y == '=':
                        self.values[s] = j[x + 1:]
                    s += y
            else:
                for x, y in enumerate(j):
                    if_str = ''
                    if y == '[':
                        while j[x] != ']':
                            names = ''
                            x += 1
                            if j[x].isalpha():
                                while j[x].isalpha():
                                    names += j[x]
                                    x += 1
                                if_str += self.values[names]
                                if not j[x].isalpha() and ']' not in j[x]:
                                    if_str += j[x]
                            else:
                                if_str += j[x]
                        if if_str[len(if_str) - 1] == ']':
                            if_str = if_str[:-1]
                        tr = tree(if_str)
                        root = tr.add()
                        print('=\n' * 3)
                        tr.preorder(root)
                        print('===== Result: ', tr.answer(), '=====')
                        print('=\n' * 3)


x = file_parse('code.txt')
