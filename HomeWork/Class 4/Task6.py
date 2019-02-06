# Преобразовать массив так, чтобы сначала шли все отрицательные элементы, 
# а потом положительные(0 считать положительным). Порядок следования должен быть сохранен.

def otricat (spi):
    otri = []
    polo = []
    for i in spi:
        if i < 0:
            otri.append (i)
        else:
            polo.append (i)
    return otri + polo

def Test_otricat():
    assert otricat ([-7,9,0,0,-8,0,6]) == [-7,-8,9,0,0,0,6], 'Тест провален'
    assert otricat ([19,-20,109,18,0,-1]) == [-20,-1,19,109,18,0], 'Тест провален'
    assert otricat ([10,-3,-7,-6,6,120,0]) == [-3,-7,-6,10,6,120,0], 'Тест провален'

a = [int (i) for i in input().split()]
minus = otricat (a)
print(minus)
Test_otricat()