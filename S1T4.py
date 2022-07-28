# 4-Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).


def incord(s):
    while 1:
        num = input(s)
        if num == '':
            continue
        elif int(num) < 1 or int(num) > 4 :
            print('Не корректный ввод')
            continue
        else:    
            return num
            break
            
numb_qvad = int(incord('Номер четверти - '))

dict_qvad = {1:'x>0 y>0', 2:'x>0 y<0', 3:'x<0 y<0', 4:'x<0 y>0'}

print(dict_qvad[numb_qvad])            
