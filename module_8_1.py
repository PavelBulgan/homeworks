def add_everything_up(a, b):
    try:
        rezult = a + b
    except TypeError as exc:
        print(f'Ошибка: {exc},\nНедопустимые типы переменных: {type(a)} , {type(b)}')
    else:
        print(f'Код сработал. результат:')
        return rezult


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up('яблоко ', 'червивое'))
print(add_everything_up(123.456, 7))
