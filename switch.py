from custom.func import *
import os
os.system('cls')


print_ln(_ln_=True, _digits_=4)


def add(a, b):
    print_ln(f'a = {a}  b= {b}\tadd(a,b)= {a+b}')


def sub(a, b):
    print_ln(f'a = {a}  b= {b}\tsub(a,b)= {a-b}')


def mult(a, b):
    print_ln(f'a = {a}  b= {b}\tmult(a,b)= {a*b}')


def div(a, b):
    print_ln(f'a = {a}  b= {b}\tdiv(a,b)= {a/b}')


def print_hello():
    print_ln(f'               \tprint_hello()= "Hello"')
    return 'Hello'


math_func = {'a': lambda: add(x, y), 's': lambda: sub(x, y),
             'm': lambda: mult(x, y), 'd': lambda: div(x, y),
             'x': print_hello}

x, y = (9, 3)
math_func['a']()
math_func['s']()
math_func['m']()
math_func['d']()
math_func['x']()

print_ln('#'*42)

x, y = (6, 2)
math_func['a']()
math_func['s']()
math_func['m']()
math_func['d']()
math_func['x']()

print_ln('#'*42)

x, y = (8, 2)
f = 'a'
{'a': lambda: add(x, y), 's': lambda: sub(x, y),
 'm': lambda: mult(x, y), 'd': lambda: div(x, y),
 'x': print_hello}[f]()

f = 's'
{'a': lambda: add(x, y), 's': lambda: sub(x, y),
 'm': lambda: mult(x, y), 'd': lambda: div(x, y),
 'x': print_hello}[f]()

f = 'm'
{'a': lambda: add(x, y), 's': lambda: sub(x, y),
 'm': lambda: mult(x, y), 'd': lambda: div(x, y),
 'x': print_hello}[f]()

f = 'd'
{'a': lambda: add(x, y), 's': lambda: sub(x, y),
 'm': lambda: mult(x, y), 'd': lambda: div(x, y),
 'x': print_hello}[f]()

f = 'x'
{'a': lambda: add(x, y), 's': lambda: sub(x, y),
 'm': lambda: mult(x, y), 'd': lambda: div(x, y),
 'x': print_hello}[f]()

print_ln('#'*42)

d = {'a': lambda: add(x, y), 's': lambda: sub(x, y),
     'm': lambda: mult(x, y), 'd': lambda: div(x, y),
     'x': print_hello}

x, y = (4, 2)
d['a']()

x, y = (6, 3)
d['s']()

print_ln('#'*42)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("price")
print_ln(x)
print_ln(car)

x = car.get("price", "key of price doesn't exist")
print(x)
print(car)

print_ln('#'*42)
