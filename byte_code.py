import dis
import os
os.system('cls')

y = 1


def example():
    global y
    y = 1.0
    for n in range(20):
        y = y * 1.5
    return y


dis.dis(example)
