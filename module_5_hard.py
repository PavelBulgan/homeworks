class User:                            # аннотации к переменным обязательны для облегчения дальнейшей работы
    def __init__(self, nickname: str, password: str, age: int):    # конструктор класса: создание класса User с тремя атрибутами
        self.nickname = nickname
        self.password = hash(password)                             # атрибут password хранится в хешированном значении
        self.age = age

    def __str__(self):
        return f'current_user: {self.nickname}'


class Video:
    def __init__(self, title: str, duration: int, time_now=0, adult_mode=False):        # Создание класса Video
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


class UrTube:                                    # Создаем класс UrTube

    def __init__(self):                          # конструктор класса: создаем атрибуты экземпляров класса
        self.users: list[User] = []              # атрибут users содержит атрибуты каждого класса User в виде списка.
        self.videos: list[Video] = []            # атрибут videos содержит атрибуты каждого класса Video в виде списка.
        self.current_user: User|None = None      # пояснения к аннотации current_user: принимает значение либо None, либо объект класса User


    def register(self,nickname: str, password: str, age: int):
        for user in self.users:                                  # перебираем объекты User из списка users
            if nickname == user.nickname:                        # проверям, не используется ли кем-то введеный nickname
                print(f'логин {nickname} занят')
                return
        user = User(nickname, password, age)                     # после удачной проверки User-у присваивается значение переменных
        self.users.append(user)                                  # данные о новом user-е записываем в класс User
        self.current_user = user                                 # присваиваем этому user-у значение текущий user


    def log_in(self,nickname: str, password: str):
        for user in self.users:
            if nickname == user.nickname:
                if hash(password) == user.password:
                    print(f'Приветствую {nickname}')
                    self.current_user = user
                else:print(f'Пароль для пользователя {nickname} указан не верно')
            else:print(f'Пользователь {nickname} не найден \n')

    def log_out(self):
        self.current_user = None

    def add(self, *new_videos):
        for added_video in new_videos:
            if added_video not in self.videos:
                self.videos.append(added_video)


    def get_videos(self, title: str):
        self.find_list_videos: list = []
        for video in self.videos:
            if title.lower() in video.title.lower():
                    self.find_list_videos.append(video.title)
            if video.title.lower() in title.lower():
                    self.find_list_videos.append(video.title)
        return self.find_list_videos

    def watch_video(self, title: str):
        import time
        current_video = None
        for video in self.videos:
            if video.title == title:
                current_video = video
        if not current_video:
            print('такого видео не существует')
            return
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return
        if current_video.adult_mode == True:                # Можно сократить без True
           if self.current_user.age < 18:
               print('Вам нет 18 лет, пожалуйста покиньте страницу')
               return
        print(f'Просмотр видео: {current_video.title}')
        a = 0
        while a <= current_video.duration:
            time.sleep(1)
            print(a, end=' ')
            a = a + 1
        print('Конец видео')



ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
v3 = Video('Как выжить в этом мире?', 15)
#
# Добавление видео
ur.add(v1, v2, v3)
#
# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')
#
# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
#
# # Попытка воспроизведения несуществующего видео
ur.watch_video('Как выжить в этом мире?')