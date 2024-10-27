def custom_write(file_name, strings):
    strings_positions = {}
    string_line = 0
    file = open(file_name, 'a', encoding='utf-8')
    for string in strings:
        start_number_baits = file.tell()
        file.write(string + '\n')
        string_line += 1
        coord = (string_line, start_number_baits)
        strings_positions.update({coord: string})
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test_7_2.txt', info)
for elem in result.items():
    print(elem)
