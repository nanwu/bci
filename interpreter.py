def interpret(code_obj):
    stack = deque()
    code = code_obj.co_code
    consts = code_obj.co_consts
    varnames = code_obj.co_varnames
    names = code_obj.co_names
    cellvars = code_obj.co_cellvars
    freevars = code_obj.co_freevars

    name_map = {}

    i = 0 
    n = len(code)
    while i < n:
        op = code[i]
        op_name = opnames[op]
        i += 1
        if op >= dis.HAVE_ARGUMENT:
            arg = code[i] | (code[i+1] << 8)
            i += 2

            if op_name == 'LOAD_CONST':
                stack.append(consts[arg])
            elif op_name == 'LOAD_NAME':
                stack.append(name_map[names[arg]])
            elif op_name == 'STORE_NAME':
                names[arg] = stack.pop()
            elif op_name == 'LOAD_BUILD_CLASS':
                stack.append(__build_class__())
            elif op_name == 'CALL_FUNCTION':
            elif op_name == 'RETURN':
                top = stack.pop()

