from collections import deque
from opcode import opmap, opname
import dis
from builtins import __build_class__


from stackframe import StackFrame

op_code = opmap.get

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
    kw
    for _ in range(kw_args_num):
        
        

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
    if func_name in name_map
    func_code = name_map[func_name] # TOS is function name
    result = interpret(func_code, _globals, args, kwargs)
    stack.append(result)


def import_name():
    module_name = co_names[oparg]
    fromlist = stack.pop()
    level = stack.pop()
    stack.append(__import__(module_name, fromlist, level))
