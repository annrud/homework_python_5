# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

with open('initial.txt', 'r') as f:
    lst = f.read().split(' ')

with open('corrected.txt', 'w') as f:
    f.write(
        ' '.join(list(filter(lambda b, a='абв', : a not in b, lst)))
    )
