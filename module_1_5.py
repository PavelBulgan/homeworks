immutable_var = 'car', 156, True
print(immutable_var)
print(immutable_var[1])
print(type(immutable_var))

#immutable_var[0] = ('plane')
#print(immutable_var)
#команда кортежа не поддерживает изменение его элементов

immutable_var = (['f', 'd'], 'dd')
print(immutable_var)
immutable_var[0][1] = 'b'
#изменяем символ d в списке кортежа на b
print(immutable_var)

mutable_list = ['volvo', 'nissan', 'bmw', 'dodge', 'lifan']
print('Начальный список: ')
print(mutable_list)
mutable_list[1] = 'TOYOTA'
mutable_list[3] = 'GMC'
print('Измененный список: ')
print(mutable_list)



