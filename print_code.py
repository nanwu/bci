import dis
from opcode import opname, opmap

with open('test.py', 'rb') as f:
    code_obj = compile(f.read(), 'test.py', 'exec')
    try:
        code = code_obj.co_code
    except AttributeError:
        sys.exit("Code is not found in test.py file.")

i = 0
n = len(code)
while i < n:
    b = code[i]
    i += 1
    if b >= dis.HAVE_ARGUMENT:
        arg = code[i] | code[i+1] << 8
        print(opname[b], '\t', arg)
        i += 2
    else:
        print(opname[b])

