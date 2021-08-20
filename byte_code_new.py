import dis
import os
os.system('cls')


def absolute_func(x):
    if x > 0:
        return x
    else:
        return -x


print(absolute_func(4))
print(absolute_func(-4))
print()

print(absolute_func)
print()

print(dis.dis(absolute_func))
print()

print(absolute_func.__code__)
print()

print(absolute_func.__code__.co_code)
print()

print(list(absolute_func.__code__.co_code))
print()

for code in dis.get_instructions(absolute_func):
    print(code)
print()


# https://www.youtube.com/watch?v=mE0oR9NQefw
# https://docs.python.org/3/library/inspect.html
