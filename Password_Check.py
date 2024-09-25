class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password

class User:
    '''
    Класс пользователя, содержащий атрибуты логин и пароль
    '''
    def __init__(self, username, password, password_conf):
        a1, a2, = 0, 0
        for i in password:
            if (i.isupper()):
                a1 = 1
        for i in password:
            if (i.isdigit()):
                a2 = 1
        if (password == password_conf) and (a1 == 1 and a2 == 1):
            self.username = username
            self.password = password
            print('Пароль введен верно')
        if (password != password_conf):
            print('Пароли не совпадают')
            exit()
        if (a1 == 0):
            print('В пароле должна быть хотя бы одна заглавная буква')
            exit()
        if (a2 == 0):
            print('В пароле должна быть хотя бы одна цифра!')
            exit()



if __name__ == '__main__':

    database = Database()
    while True:
        choice = int(input('Хайлюшки. Выбери че нить: \n1 - Регистрация \n2 - Вход \n'))
        if choice == 2:   # Вход
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Приветствую {login}')
                    break
                else:print(f'Пароль для пользователя {login} указан не верно.')
            else:print(f'Пользователь {login} не найден \n')
        if choice == 1:   # Регистрация
            user = User(input('Введите логин: '), input('Введите пароль: '), input('Повторите ввод пароля: '))
            database.add_user(user.username, user.password)
            print(database.data)