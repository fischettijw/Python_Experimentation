from custom.func import *


@speed_test
def sum_nums_gen():
    return sum(x for x in range(100_000_000))


@speed_test
def sum_nums_list():
    return sum([x for x in range(100_000_000)])


print_ln(sum_nums_gen())
print_ln(sum_nums_list())
print_ln()
print_ln('*'*40)
