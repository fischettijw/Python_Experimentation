from custom.func import *
import dis
import os
os.system('cls')


def absolute_func(x):
    if x > 0:
        return x
    else:
        return -x


print_ln(absolute_func(4))
print_ln(absolute_func(-4))
print_ln()

print_ln(absolute_func)
print_ln()

print_ln(dis.dis(absolute_func))
print_ln()

print_ln(absolute_func.__code__)
print_ln()

print_ln(absolute_func.__code__.co_code)
print_ln()

print_ln(list(absolute_func.__code__.co_code))
print_ln()

for code in dis.get_instructions(absolute_func):
    print_ln(code)
print_ln()


# https://www.youtube.com/watch?v=mE0oR9NQefw
# https://docs.python.org/3/library/inspect.html
