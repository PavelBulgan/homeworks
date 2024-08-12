first = int(input('Первое число: '))
second = int(input('Второе число: '))
third = int(input('Третье число: '))
if first == second == third:
    print('все числа равны друг другу')
elif first == second or second == third or first == third:
    print('2 числа равны')
else:
    print('нет равных чисел')