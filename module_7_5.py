import os
import time
directory = r'C:\Users\pbulg\PycharmProjects\pythonProject\module_1'
for root, dirs, files in os.walk(directory):
    for file_name in files:
        filepath = root
        file = os.path.join(r'C:\Users\pbulg\PycharmProjects\pythonProject\module_1', file_name)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime('%d.%m.%Y %H:%M', time.localtime(filetime))
        file_size = os.path.getsize(file)
        parent_dir = os.path.dirname(file)
        print(f'Обнаружен файл: {file_name}, Путь: {filepath}, Размер: {file_size} байт, Время изменения: {formatted_time}, '
              f'Родительская директория: {parent_dir}')
