# 5- Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def incord(s):
    while 1:
        num = input(s)
        if num == '':
            continue
        else:    
           return num
           break

A_x = int(incord('Точка A  х = '))
A_y = int(incord('Точка A  y = '))
B_x = int(incord('Точка B  х = '))
B_y = int(incord('Точка B  y = '))
AB = ((B_x - A_x) ** 2 + (B_y - A_y ) ** 2) ** 0.5
print(AB)