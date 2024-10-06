# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
immutable_var = 34, 3.14, 'Strig example', True, [1,2,3,4,5,6,7]

#   - Выполните операции вывода кортежа immutable_var на экран.
print('Immutable tuple: ', immutable_var)

#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
# immutable_var[4] = 3 - это выражение вызовет ошибку т.к. кортеж - неизменяемый тип
immutable_var[4][0] = 3 # в данном случае я изменяю не кортеж, а список
print(immutable_var)

#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
mutable_list = [1, 2, 'a', 'b', 'text']
print('Mutable list: ', mutable_list)
mutable_list[-1] = 'Modified'
mutable_list[0] = -1000.1
print('Mutable list: ', mutable_list)
