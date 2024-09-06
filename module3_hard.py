data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
def sum_data_structure(*args):
    elem_sum = 0
    for elem in args:
        if isinstance(elem, int):
            elem_sum = elem + elem_sum
        elif isinstance(elem, str):
            elem_sum = len(elem) + elem_sum
        elif isinstance(elem, (list, tuple, set)):
            for i in elem:
                elem_sum = elem_sum + sum_data_structure(i)
        elif isinstance(elem, dict):
            for key, value in elem.keys(), elem.values():
                elem_sum = elem_sum + sum_data_structure(key) + sum_data_structure(value)
    return elem_sum

print(sum_data_structure(data_structure))
