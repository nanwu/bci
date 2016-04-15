import dis

with open('test.py', 'r') as f:
    code = compile(f.read(), 'test.py', 'exec')
    print(code.co_varnames)
    print(code.co_names)
    print(dis.dis(code.co_consts[0]))
