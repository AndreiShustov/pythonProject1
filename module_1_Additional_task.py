# Дополнительное практическое задание по модулю: "Базовые структуры данных."
# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную средний
# балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
#
# На вход даны следующие данные:
#
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.
# Вывод в консоль:
# {'Aaron': 4.0, 'Bilbo': 2.25, 'Johhny': 4.0, 'Khendrik': 3.6666666666666665, 'Steve': 4.8}

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students= list(students)    # преобразуем множество в список
students.sort()             # отсортируем список по алфавиту

average_rating = list()     # создадим список средних баллов для каждого ученика
average_rating.append(sum(grades[0]) / len(grades[0]))
average_rating.append(sum(grades[1]) / len(grades[1]))
average_rating.append(sum(grades[2]) / len(grades[2]))
average_rating.append(sum(grades[3]) / len(grades[3]))
average_rating.append(sum(grades[4]) / len(grades[4]))

dict_of_grades = dict()     # создадим словарь учеников и их средний балл
dict_of_grades.update({students[0]: average_rating[0]})
dict_of_grades.update({students[1]: average_rating[1]})
dict_of_grades.update({students[2]: average_rating[2]})
dict_of_grades.update({students[3]: average_rating[3]})
dict_of_grades.update({students[4]: average_rating[4]})

print(dict_of_grades)       # Выведем в консоль словарь