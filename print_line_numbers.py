# https://www.youtube.com/watch?v=jiPalxUAlUg&list=PL1e1htFlLTtHZI2qQPNLkPo0tLLO46_ym
# C:\Users\fisch\AppData\Roaming\Python\Python39\site-packages

from custom.func import *
import os
os.system('cls')

print_ln(_ln_=True, _digits_=4)

a = ('a', 'b', 'c', 'd', 'e')
b = (1, 2, 3, 4, 5)
print_ln(a)
d = dict(zip(a, b))
print_ln(d)
print_ln(b)
print_ln()

for _ in range(4):
    print_ln(f'{_} - Hello')
print_ln()

print_ln(a)
for x, y in enumerate(a):
    print_ln(x, y)
print_ln(a)

for x, a in enumerate(a):
    print_ln(x, a) if x != 2 else print_ln("x = 2")
print_ln('\n\n')


def test(*args, kw1=14, **kwargs):
    print_ln(args, kwargs, kw1)


test()
test(k=2)
test(3, k=2, _on_=45)
print_ln('\n\n')
