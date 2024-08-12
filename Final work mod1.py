grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# print(type(students))
students = dict.fromkeys(students, 0)  # преобразование из множества в словарь
# print(type(students))
# print(students)
sorted_students = dict(sorted(students.items()))  # Сортировка словаря в алфавитном порядке по ключу(имени)
sorted_students.update({'Johnny': (sum(grades[2])) / (len(grades[2])), 'Bilbo': (sum(grades[1])) / (len(grades[1])),
                        'Steve': (sum(grades[4])) / (len(grades[4])), 'Khendrik': (sum(grades[3])) / (len(grades[3])),
                        'Aaron': (sum(grades[0])) / (len(grades[0]))})
print('Средний балл учеников: ', sorted_students)
