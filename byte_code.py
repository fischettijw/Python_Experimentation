# region identification#

# Programmer:   Joseph Fischetti
# Language:     Python

# endregion identification

# region Links
# https://www.youtube.com/watch?v=PJ16cdc0YKM
# https://docs.python.org/3/library/dis.html
# endregion Links

# region Imports

from custom.func import *
import dis
import os

# endregion Imports

# region Global Variables

# endregion Global Variables

# region functions


def cls():
    os.system('cls')


def wait_for_keypress(prnt=""):
    input(prnt)


def print_bytecode(inst):
    pass


def myfunc(myarg):
    if myarg != 0:
        print(myarg)


'''
                        0           1         2         3               4               5           6               7
Instruction(opname='LOAD_FAST', opcode=124, arg=0, argval='myarg', argrepr='myarg', offset=0, starts_line=41, is_jump_target=False)    
Instruction(opname='LOAD_CONST', opcode=100, arg=1, argval=0, argrepr='0', offset=2, starts_line=None, is_jump_target=False)
Instruction(opname='COMPARE_OP', opcode=107, arg=3, argval='!=', argrepr='!=', offset=4, starts_line=None, is_jump_target=False)       
Instruction(opname='POP_JUMP_IF_FALSE', opcode=114, arg=16, argval=16, argrepr='', offset=6, starts_line=None, is_jump_target=False)   
Instruction(opname='LOAD_GLOBAL', opcode=116, arg=0, argval='print', argrepr='print', offset=8, starts_line=42, is_jump_target=False)  
Instruction(opname='LOAD_FAST', opcode=124, arg=0, argval='myarg', argrepr='myarg', offset=10, starts_line=None, is_jump_target=False) 
Instruction(opname='CALL_FUNCTION', opcode=131, arg=1, argval=1, argrepr='', offset=12, starts_line=None, is_jump_target=False)        
Instruction(opname='POP_TOP', opcode=1, arg=None, argval=None, argrepr='', offset=14, starts_line=None, is_jump_target=False)
Instruction(opname='LOAD_CONST', opcode=100, arg=0, argval=None, argrepr='None', offset=16, starts_line=None, is_jump_target=True)     
Instruction(opname='RETURN_VALUE', opcode=83, arg=None, argval=None, argrepr='', offset=18, starts_line=None, is_jump_target=False)
'''


def print_dis():
    def print_line(ins):
        print(ins)
        print(type(ins[6]))
        print(f'{ins[6]:03}\t\t{ins[5]} {ins[1]}\t\t\t{ins[2]}')
        # print(f'{inst[5]}')
        print()

    for inst in dis.get_instructions(myfunc):

        # print_line(inst) if inst[6] != None else print()
        print_line(inst)
    # input()


# endregion Function

# region main function


def main():
    cls()

    # dis.dis(myfunc)  # no retunr - only prints
    print()
    # wait_for_keypress(f"\n\n {'='*50}\n")
    # input()

    # for inst in dis.get_instructions(myfunc):
    #     #     print(inst)
    #     #     # print(inst[1])
    print_dis()
    # input()

    # print(f"\n {'='*50}\n")


# endregion main function

if __name__ == '__main__':
    main()
