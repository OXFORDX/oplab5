# Alpha version of parsing
container = []
values = {}
parameters = {'condition': 0, 'then': 0, 'else': 0}
with open('code.txt', 'r') as file:
    for i in file:
        if '\n' in i:
            container.append(i[:-1].replace(' ', ''))
        else:
            container.append(i.replace(' ', ''))
print(container)
for i, j in enumerate(container):
    print('--')
    s = ''
    if 'if' not in j:
        for x, y in enumerate(j):
            if y == '=':
                values[s] = int(j[x + 1:])
            s += y
            print(x, y)
    else:
        if_cont = []
        const = 0
        for x, y in enumerate(j):
            if_str = ''
            if y == '(':
                while j[x + 1] != ')':
                    x += 1
                    if_str += j[x]
                if const == 0:
                    parameters['condition'] = if_str
                elif const == 1:
                    parameters['then'] = if_str
                else:
                    parameters['else'] = if_str
                const += 1
print(values)
print(parameters)


