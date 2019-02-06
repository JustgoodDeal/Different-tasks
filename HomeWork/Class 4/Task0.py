# Написать программу, которая предлагает пользователю ввести список чисел,
# после чего  запрашивает число для которого нужно посчитать сколько раз оно встречается в списке.

def repetitions (a,x):
    repeat = 0
    for i in a:
        if i == x:
            repeat+=1
    return repeat

def Test_repetitions ():
    assert repetitions([10, 20, 2, 2, 55, 47], 2) == 2 , 'Тест провален'
    assert repetitions([0, 7, 8, 3], 2) == 0 , 'Тест провален'
    assert repetitions([10, 10, 3, 3, 3, 20, 2, 2, 55, 47], 3) == 3 , 'Тест провален'

repeat = repetitions ([int (i) for i in input().split()], int (input()))
print (repeat)
Test_repetitions ()



