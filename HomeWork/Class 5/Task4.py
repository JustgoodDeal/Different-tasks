# Дана квадратная матрица А(N,N). Составить программу подсчета 
# количества положительных элементов, расположенных выше главной диагонали.

import random

def count_above(A, N):
    for raw in A:
        print (' '.join([str(i) for i in raw]))
    count=0
    for i in range (N):
        for j in range (i+1,N):
            if A[i][j]>0:
                count+=1
    return count

def Test_count_above():
    assert count_above ([[4,10,3],[7,-3,-5],[-8,6,-1]],3) == 2, 'Тест провален'
    assert count_above ([[4,10,3,-9],[7,-3,-5,2],[-8,6,-1,3],[0,1,2,-3]],4) == 4, 'Тест провален'

N = int(input())
A = [[random.randrange(-100,100) for y in range(N)] for x in range(N)]
print('Матрица:')
count = count_above(A,N)
print('Количество положительных элементов, удовлетворяющих условию: \n' +str(count))
Test_count_above()




