def print_params( a = 1, b = 'строка', c = True):
#    print(a)
#    print(a, c)
    print(a, b, c)
#    print()

print_params(b=25)
print_params(c=[1, 2, 3])
values_list = ['список', False, 568]
values_dict = {'a': 2, 'b': 'словарь', 'c': True}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ['2 элемента', 123]
print_params(*values_list_2, 42)