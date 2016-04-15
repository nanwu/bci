def return_value():
    return stack.pop()

def load_const():
    stack.append(consts[oparg])

def load_name():
    stack.append(name_map[names[oparg]])

def store_name():
    names[arg] = stack.pop()

def load_build_class():
    stack.append(__build_class__())


def make_function():
    func_name = stack.pop()
    func_code = stack.pop()

    param_names = None
    param_annotations = deque()   
    param_annotations_num = oparg >> 16 & 0x7fff
    if param_annotations_num:
        param_names = stack.pop() # param_names is tuple
        for _ in range(param_annotations_num):
            param_annotations.appendleft(stack.pop())

    kw_arg_num = oparg >> 8 & 0xff
        
        

def call_function():
    pos_args_num = 0xff & oparg
    kw_args_num = 0xff & oparg >> 8

    args = deque()
    kwargs = dict()

    for _ in range(kw_args_num):
        v, k = stack.pop(), stack.pop()
        kwargs[k] = v
    
    for _ in range(pos_args_num):
        pos_args.appendleft(stack.pop())

    func_name = stack.pop()
    try:
        func_code = name_map[func_name] # TOS is function name
    except KeyError: # built-in function 
        func_code = _globals[func_name]

    result = interpret(func_code, _globals, args, kwargs)
    stack.append(result)


def import_name():
    module_name = co_names[oparg]
    fromlist = stack.pop()
    level = stack.pop()
    stack.append(__import__(module_name, fromlist, level))
