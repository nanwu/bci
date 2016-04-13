from opcode import opmap
import dis


op_code = opmap.get

def interpret(code):
    stack = []
    i = 0
    n = len(code)
    while i < n:
        op = code[i]
        i += 1
        if ord(op) >= dis.HAVE_ARGUMENT:
            arg = code[i] | (code[i+1] << 8)
            i += 2

            if op_code('LOAD_FAST') == op:
                stack.append(arg)   
            elif op_code('RETURN_VALUE') == op:
                top = stack.pop()

        else:



print "-- dis output below --"
dis.dis(add)
