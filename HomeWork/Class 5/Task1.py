# Дана целая матрица А(N,N). Составить программу подсчета среднего арифметического значения элементов матрицы.

import random
from Mod.module_1 import srednee_arif
from Mod.module_1 import Test_srednee_arif

N = int (input())
A = [[random.randrange(-100,100) for y in range(N)] for x in range(N)]
print('Матрица:')
for raw in A:
    print (' '.join([str(i) for i in raw]))
itog = srednee_arif(A,N)
print ('Среднее арифметическое значение элементов: ' + str(itog))
Test_srednee_arif ()
