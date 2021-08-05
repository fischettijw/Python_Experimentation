from custom.func import *
import os
os.system('cls')

print_ln(_ln_=True, _digits_=4)


@exception_handler
def test(x, *args, on=14, **kwargs):
    print_ln(args, kwargs, on, x)


test(12)
test(k=2)
test(3, k=2, _on_=45)
