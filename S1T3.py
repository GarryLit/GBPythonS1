# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и 
# выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).


from ast import Continue


def incord(s):
    while 1:
        num = (input (s))
        if num == '0' or num == '' :
            print('Координата не должна быть равна нулю')
            continue
        else:    
            return num
            break

x = int(incord('X = '))
y = int(incord('Y = '))
print(x)
print(y)
numb_qvad = 4

if x > 0 and y > 0:
    numb_qvad = 1
elif x < 0 and y > 0:
    numb_qvad = 2
elif x < 0 and y < 0:
    numb_qvad = 3
    
print(f" {numb_qvad} четверть плоскости")
