# Дан список чисел. Создать функцию, которая вычисляет сумму элементов списка, если в нем 2 элемента. 
# Если же элементов больше, то результат работы функции следующий: сумма первых двух элементов списка + сумма
# остальных элементов, деленная на их минимальное зачение.

def calc (*arg):
    if len(arg) == 2:
        return arg[0]+arg[1]
    else:
        spi=arg[2:]
        mini = min(spi)
        if mini==0 and mini in spi:
            return 'Ошибка деления'
        else:
            sum=0
            for i in spi:
                sum+=i
            return arg[0]+arg[1]+sum/mini

def Test_calc ():
    assert calc (1,2,8,1,8) == 20 , 'Тест провален'
    assert calc (10,22) == 32 , 'Тест провален'
    assert calc (10,22,13) == 33 , 'Тест провален'
    assert calc (1,2,13,0) == 'Ошибка деления' , 'Тест провален'
    assert calc (1,2,10,-2,6) == -4 , 'Тест провален'

itog = calc (*[int (i) for i in input().split()])
print (itog)
Test_calc ()

