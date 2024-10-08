# Практическое задание по уроку "Строки и индексация строк"
# Цель: Научиться работать со строками и индексацией строк в Python.
# Задача:
# В переменную example запишите любую строку
example = 'Python'
# Выведите на экран(в консоль) первый символ этой строки.
print(example[0])

# Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
print(example[-1])

# Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
print(example[3:])

# Выведите на экран(в консоль) это слово наоборот.
print(example[::-1])

# Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
print(example[1::2])

example = 'Топинамбур'
print(example[1::2])
