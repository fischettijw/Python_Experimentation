import sys
import traceback
import inspect
import time as tm
from functools import wraps
import os
os.system('cls')

__print_linenumbers__ = True
__default_digits = 3
__digits__ = __default_digits


def print_ln(*args, _ln_=True, _digits_=__digits__, **kwargs):
    global __print_linenumbers__, __digits__
    if args == () and kwargs == {}:
        __print_linenumbers__ = _ln_
    if args == () and kwargs == {} and _digits_ != __default_digits:
        __digits__ = _digits_
    if(__print_linenumbers__):
        caller = inspect.getframeinfo(inspect.stack()[1][0])
        print(f"{caller.lineno:{'0'+str(__digits__)}} -", *args, **kwargs)
    else:
        print(*args, **kwargs)


def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(f"{func.__name__} - {e}")
            print(f'Line Number: {tb[1]}\n')
    return inner_function


def speed_test(fn):
    @wraps(fn)    # https://www.youtube.com/watch?v=6LZeIeoa5kI
    def wrapper(*args, **kwargs):
        start_time = tm.time()
        result = fn(*args, **kwargs)
        end_time = tm.time()
        print()
        print(f'Executing {fn.__name__}')
        print(f'Time Elapsed: {end_time - start_time}')
        return result
    return wrapper


def main():
    print_ln(_ln_=True, _digits_=6)
    print_ln('hello', 'goodbye', end='\n\n\n')
    print_ln()
    print_ln(_ln_=False)
    print_ln('hello', 'goodbye', end='\n\n')


if __name__ == '__main__':
    main()
