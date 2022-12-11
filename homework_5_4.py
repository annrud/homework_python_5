# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
subsequence = input('Введите RLE последовательность, например, aaabbc: ')


def run_length_encoding(string):
    char, count = string[0], 0
    encoding_str = ''
    for i in string:
        if char != i:
            encoding_str += str(count) + char
            char, count = i, 1
        else:
            count += 1
    encoding_str += str(count) + char
    return encoding_str


print('Сжатие данных:', run_length_encoding(subsequence))


def recovery(string):
    recovery_str = ''
    count = '0'
    for i in range(len(string)):
        char = string[i]
        if char.isdigit():
            count += char
        else:
            recovery_str += char * int(count)
            count = '0'
    return recovery_str


str_for_recovery = run_length_encoding(subsequence)
print('Восстановление данных:', recovery(str_for_recovery))
