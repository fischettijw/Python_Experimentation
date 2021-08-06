import dis
import os


def cls():
    os.system('cls')


def myfunc(myarg):
    if myarg != 0:
        print(float(myarg))
        return myarg * 2


cls()
dis.dis(myfunc)
input(f"\n {'='*50}\n")

os.system('cls')
for inst in dis.get_instructions(myfunc):
    print(inst)
input(f"\n {'='*50}\n")