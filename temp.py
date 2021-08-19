def concatebator(a, b):
    return a + b


print(concatebator)

print(concatebator.__code__.co_code)
print(list(concatebator.__code__.co_code))
print()
