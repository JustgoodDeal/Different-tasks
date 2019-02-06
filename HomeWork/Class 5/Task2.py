# Дана вещественная матрица А(3,4). Составить программу подсчета количества элементов матрицы,
# удовлетворяющих условию р1<=a(i,j)<=p2. Значения р1 и р2 запрашиваются у пользователя. 

import random
from Mod.module_2 import *
    
N = 3
M = 4
A = [[random.randrange(-100,100) for y in range(M)] for x in range(N)]
count = count_if(A,p1 = int(input()),p2 = int(input()))
print('Матрица:')
for raw in A:
    for j in raw:
        print (j,end=' ')
    print()
print('Количество элементов матрицы, удовлетворяющих условию: \n' +str(count))
Test_count_if()        
