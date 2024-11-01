data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
    ]

def calculate_structure_sum(data_structure):
    numbers = 0
    symbols = 0

    data_structure_list = str(data_structure)
    symbols_to_remove = "'[]{},:'()"
    for i in symbols_to_remove:
        data_structure_list = data_structure_list.replace(i, "")
    data_structure_split = data_structure_list.split()

    for i in data_structure_split:
        if i.isdigit():
            numbers += int(i)
        else:
            symbols += len(i)

    return numbers+symbols

result = calculate_structure_sum(data_structure)
print(result)

