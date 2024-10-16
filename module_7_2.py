def custom_write(file_name, strings):
    strings_positions = {}
    string_line = 0
    for string in strings:
        file = open(file_name, 'a', encoding='utf-8')
        start_number_baits = file.tell()
        file.writelines([string + '\n'])
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

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
