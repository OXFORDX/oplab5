from my_array import Stack


class polish:
    def __init__(self, formula):
        self.OPERATORS = {'+': (1, lambda x, y: x + y), '-': (1, lambda x, y: x - y),
                          '*': (2, lambda x, y: x * y), '/': (2, lambda x, y: x / y),
                          '^': (3, lambda x, y: x ** y), '!': (3, lambda x: self.fact(x)),
                          '~': (3, lambda x: self.bino(x))}
        self.formula = formula
        self.result = self.calc()

    def fact(self, x):
        if x == 1:
            return x
        return x * self.fact(x - 1)

    def bin(self, x):
        return int(bin(x)[2:][::-1], 2)

    def parse(self, formula):
        stack_in = []
        num = ''
        for item in formula:
            if item in self.OPERATORS or item in '()':
                if num:
                    stack_in.append(int(num))
                stack_in.append(str(item))
                num = ''
            elif item.isdigit():
                num += item
        if num:
            stack_in.append(int(num))
        minus = 0
        while True:
            try:
                if stack_in[minus] == '-':
                    if stack_in[minus + 1] == stack_in[minus]:
                        stack_in[minus] = '+'
                        stack_in.pop(minus + 1)

                minus += 1
            except IndexError:
                return stack_in

    def factotial(self, formula):
        li = self.parse(formula)
        i = len(li) - 1
        while True:
            if i < 1:
                break
            if str(li[i]) == '!':
                li[i - 1] = self.OPERATORS['!'][1](li[i - 1])
                li.pop(i)
            i -= 1
        return li

    def bino(self, formula):
        li = self.factotial(formula)
        i = len(li) - 1
        while True:
            if i == 0:
                break
            if str(li[i - 1]) == '~':
                li[i] = self.OPERATORS['~'][1](li[i])
                li.pop(i - 1)

            i -= 1
        return li

    def negative_zero(self, formula):
        li = self.bino(formula)
        i = 0
        while True:
            if i == len(li) - 1:
                break

            if str(li[i]) in '/*' and li[i + 1] == '-':
                li[i + 1] = int(-1)
                li.insert(i + 2, '*')

            if li[0] == '-':
                li.pop(0)
                li[0] = li[0] * -1
            i += 1
        return li

    def polish(self, formula):
        stack_in = self.negative_zero(formula)
        stack_oper = Stack()
        out = []
        for item in stack_in:
            if item in self.OPERATORS:
                if stack_oper.isEmpty() or str(stack_oper.peek()) in '()':
                    stack_oper.push(item)
                elif self.OPERATORS[str(item)][0] == self.OPERATORS[str(stack_oper.peek())][0]:
                    out.append(stack_oper.pop())

                    stack_oper.push(item)
                elif self.OPERATORS[str(item)][0] > self.OPERATORS[str(stack_oper.peek())][0]:
                    stack_oper.push(item)

                elif self.OPERATORS[str(item)][0] < self.OPERATORS[str(stack_oper.peek())][0]:
                    out.append(stack_oper.pop())
                    stack_oper.push(item)
            elif str(item) in '()':
                if item == ')':
                    x = True
                    while x:
                        out.append(stack_oper.pop())
                        if stack_oper.peek() == '(':
                            stack_oper.pop()
                            break
                else:
                    stack_oper.push(item)

            else:
                out.append(item)
        for i in range(stack_oper.size()):
            out.append(stack_oper.pop())
        return out[::-1]

    def calc(self):
        out = self.polish(self.formula)
        st1 = Stack()
        st1.copy(out)
        working = Stack()
        z = len(out)
        for token in range(z):
            if st1.peek() in self.OPERATORS:
                z = st1.pop()
                y, x = working.pop(), working.pop()
                var = self.OPERATORS[str(z)][1](x, y)
                working.push(var)
            else:
                working.push(st1.pop())
        return working.stack[0]

    def __iter__(self):
        out = self.polish(self.formula)
        st1 = Stack()
        st1.copy(out)
        working = Stack()
        z = len(out)
        for token in range(z):
            if st1.peek() in self.OPERATORS:
                z = st1.pop()
                y, x = working.pop(), working.pop()
                var = self.OPERATORS[str(z)][1](x, y)
                working.push(var)
                yield z, x, y
            else:
                working.push(st1.pop())

    def __repr__(self):
        return repr(self.result)
