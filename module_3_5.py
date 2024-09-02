def get_multiplied_digits(number):
    str_number = str(number)  # перевод числового значения с строковое
    first = int(str_number[0])  # первый элемент от строковогозгачения переведенный в число
    if len(str_number) > 1:  # проверка на условие если длина строкового значения меньше 1
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

print(get_multiplied_digits(40203))