from collections import deque
from opcode import opmap, opname
import dis
import pprint
from builtins import __build_class__

from frame import Frame
import instructions

op_code = opmap.get
opnames = set(opmap.keys())
instruction_code = dict()

for k in dir(instructions):
    if k.upper() in opnames:
        instruction_code[k.upper()] = instructions.__dict__[k].__code__

# use deque to emulate the stack in memory
stack = deque()

def interpret(code):
    code = code.co_code
    consts = code.co_consts
    varnames = code.co_varnames
    names = code.co_names
    cellvars = code.co_cellvars
    freevars = code.co_freevars

    frame = Frame(code, consts) 
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

