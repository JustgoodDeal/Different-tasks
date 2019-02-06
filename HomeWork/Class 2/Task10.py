# Ввести три числа А,В,С. Удвоить каждое из них, если А>=В>=С, иначе поменять значения А и В

A, B, C = int (input()), int (input()), int (input())
if A>=B>=C:
    print (A*2, B*2, C*2)
else:
     print (B, A, C)