"""
Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.
"""

def total ():
    total_res = 0
    exit_q = False
    while exit_q == False:
        number = input('Введите строку чисел, разделенных пробелом или Q для выхода - ').split()
        start = 0
        for el in range(len(number)):
            if number[el] == 'q' or number[el] == 'Q':
                exit_q = True
                break
            else:
                start = start + int(number[el])
        total_res = total_res + start
        print(f'Сумма введенных чисел = {total_res}')
    print(f'Окончательная сумма введенных чисел =  {total_res}')
total()