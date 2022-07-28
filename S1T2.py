#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат


def chexpress(x, y, z):
    expression_A = not (x or y or z)
    expression_B = not x and not y and not z
    return expression_A == expression_B
   
 
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, chexpress(x,y,z))