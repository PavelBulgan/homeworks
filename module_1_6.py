print('Проверочная работа по словарям:')
list_of_debts = {'Viktor': 1500000, 'Sveta': 25000, 'my_wife': -10000000}
print(list_of_debts)
print(list_of_debts['Viktor'])
print(list_of_debts.get('my_cat'))
list_of_debts.update({'my_cat': 'Новые тапки', 'my_boss': 'Отпускные'})
print(list_of_debts)
list_of_debts.pop('my_wife')
print(list_of_debts)

print('Проверочная работа по множествам:')
my_set = {1,2,3,4,5,4,3,2,1,False,True,'string',(3,5,7,9)}
print(my_set)
my_set.update(('новые тапки', 'отпускные'))
print(my_set)
print(my_set.remove('string'))
print(my_set)

