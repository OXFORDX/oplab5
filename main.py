from file_parse import file_parse
from calc import polish

fi = file_parse('code.txt')
print(fi.parameters['condition'])
if polish(fi.parameters['condition']).result:
    print('Result1: ', polish(fi.parameters['then']).result)
else:
    print('Result2: ', polish(fi.parameters['else']).result)
