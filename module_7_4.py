team1 = 'Мастера кода'
team2 = 'Волшебники данных'
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 40
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = 'Победа команды %(name)s!' % {'name': team1}
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = 'Победа команды {name} со счетом {score}'. format(name=team2, score=score_2)
else:
    result = f'Ничья! Повторный матч команд {team1} и {team2} состоится через неделю.'

print(result)