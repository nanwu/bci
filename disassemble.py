import dis

with open('test.py', 'r') as f:
    code = compile(f.read(), 'test.py', 'exec')
    print(dis.dis(code.co_consts[0]))
